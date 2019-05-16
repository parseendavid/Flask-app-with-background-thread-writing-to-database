# Threads Get Entangled! 🤧

This mini project documents an approach to writing a background task that can access flask's db and runs periodically.

The problem being tackled here is creating the background task without using an external library like Celery or Apscheduler

To avoid intefering with the flask's serve instance a daemonized threading is used.

## Step 1. Create the task using a modified threading.Timer

threading.Timer gives the waiting functionality but does not repeat the task so let's patch it :
code in : app/background_db_task.py

```python
from threading import Timer
class RepeatTimer(Timer):
        def run(self):
            while not self.finished.wait(self.interval):
                self.function(*self.args, **self.kwargs)
```

The rest of the file is the functionality for the job.
PS. Note that we are passing a db instance to the _write\_to\_db_ function.

```python
thread = RepeatTimer(5,write_to_db, [db])
```

## Step 2. Run the task after the server process starts.
This is done on the _\_\_init\_\_.py_ file. You can run it anywhere after you instantiate the flask app.

```python
# Create a flask instance
from app.background_db_task import start_thread
start_thread(db)
```
