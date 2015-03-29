from flask import Flask
from models.Contribution import Contribution
from models.File import File
import os, sys
from peewee import *
from ingester import ingest

app = Flask(__name__)

@app.route('/')
def summary():
    text = '<h1>Database Summary</h1>\n'
    file1 = File.get(id=1)
    file2 = File.get(id=2)
    file3 = File.get(id=3)

    text += '<h2>' + file1.name + '</h2>\n'
    text += '<h2>' + file2.name + '</h2>\n'
    text += '<h2>' + file3.name + '</h2>\n'

    return text


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
    mode = sys.argv[1]
    if mode == 'run':
        app.run()
    elif mode == 'reset':
        reset_database()
