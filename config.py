import os
DEBUG = True
SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(os.path.abspath(os.path.dirname(__file__)),'app.db')}"
SQLALCHEMY_TRACK_MODIFICATIONS = False