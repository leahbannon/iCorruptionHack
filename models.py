from pprint import pprint as pp
from pymongo import MongoClient
client = MongoClient()
db = client.corruptions
contributions = db.contributions

contributions.ensure_index([("sub_id", 1), ("scraped_date", 1)], unique=True)
