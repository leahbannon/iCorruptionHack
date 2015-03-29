from models import contributions
import csv

# valid_date_combinations = [
# 	("2.17.2014", "9.14.2014"),
# 	("2.17.2014", "3.22.2015"),
# 	("9.14.2014", "3.22.2015"),
# 	("2.17.2014", "9.14.2014", "3.22.2015")
# ]

# finding deleted
grouped_by_sub_id = contributions.aggregate([{"$group": {"_id": "$sub_id", "dates": { "$push" : "$scraped_date"}}}], allowDiskUse=True, useCursor=True, batchSize=10)

with open("contributions.csv", "w") as f:
	writer = csv.writer(f)

	for contribution in grouped_by_sub_id:
		sub_id = contribution['_id']
		feb_2014 = ""
		sept_2014 = ""
		mar_2015 = ""

		for date in contribution['dates']:
			month, day, year = date.split(".")
			if month == "2" and year == "2014":
				feb_2014 = date
			elif month == "9" and year == "2014":
				sept_2014 = date
			elif month == "3" and year == "2015":
				mar_2015 = date

		row = [sub_id, feb_2014, sept_2014, mar_2015]
		print row
		writer.writerow(row)

