from flask import Flask
from models.Contribution import Contribution
from models.File import File
import os
from peewee import *
from ingester import ingest

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

def create_db():
  db = SqliteDatabase('./contributions.db')
  print("Created database 'contributions.db'")
  Contribution.create_table()
  File.create_table()
  print "Created tables"

  return db

def seed_db(db):
    # ingest
    pass

def reset_database():
  # Delete 'emails.db' sqlite database
  if os.path.exists('./contributions.db'):
    os.remove('./contributions.db')
    print("Deleted database 'contributions.db'")

  # Re-create 'emails.db' sqlite database
  db = create_db()
  seed_db(db)

if __name__ == '__main__':
    reset_database()
    # app.run()
