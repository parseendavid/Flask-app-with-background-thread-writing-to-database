# Here lies the task that periodically populate the Quotes table in the database with
# a random safe for work (mostly programming) joke from https://official-joke-api.appspot.com/jokes/random
#  Expected data shapes:
#  Example 1. 
#     {
#         "id": 56,
#         "type": "programming",
#         "setup": "How do you check if a webpage is HTML5?",
#         "punchline": "Try it out on Internet Explorer"
#     }
# 

import requests
from threading import Timer
from app.models import Joke
import time



url = "https://official-joke-api.appspot.com/jokes/random"
    

def fetch_joke(url):
    return requests.get(url).json()

def write_to_db(db):
    # Data cannot be passed as a param because it will be prefetched
    # by the thread and reused.
    try:
        data = fetch_joke(url)
        if Joke.query.filter_by(setup=data['setup']).first() is None:
            joke = Joke(_type=data['type'], setup=data['setup'], punchline=data['punchline'])
            db.session.add(joke)
            db.session.commit()
    except Exception as e :
        print(f"There was an Error: {e}")
    
def start_thread(db):
    class RepeatTimer(Timer):
        def run(self):
            while not self.finished.wait(self.interval):
                self.function(*self.args, **self.kwargs)

    # Call the write to db function every 5 seconds
    thread = RepeatTimer(5,write_to_db, [db])
    # Make thread run in the background
    thread.daemon=True
    # Start thread
    thread.start()
