"""
Analyze data in SQLite database
"""

import dateutil.parser
import datetime

from peewee import *

from models.Contribution import Contribution
from models.File import File

db = SqliteDatabase('contributions.db')
