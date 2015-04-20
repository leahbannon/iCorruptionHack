from flask import Flask
import os, sys
import json
from peewee import *

from app import app, db
from models import File, Contribution

def createtables_db():
    # Connect to our database.
    db.connect()
    
    # Create the tables.
    db.create_tables([Contribution, File])

    print "Created tables"

def clear_db():
    db.execute_sql('drop schema public cascade; create schema public;')
    print "Cleared database"

def seed_db():
    # ingest
    pass

def reset_database():
    # Drop all tables in postgres database
    clear_db()

    # Create tables
    createtables_db()

    # Seed data 
    # seed_db()

if __name__ == '__main__':
    mode = sys.argv[1]
    if mode == 'run':
        app.run()
    elif mode == 'reset':
        reset_database()
