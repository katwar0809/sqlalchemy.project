from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import Person, Activity

engine = create_engine('sqlite:///activities.db', echo=True)

