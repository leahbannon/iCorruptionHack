import csv
import json

with open('data/diff.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    header = spamreader.next()[23:]
    

    diffs = []

    for row in spamreader:
        
        diff = []

        first_half = row[:23]
        first = dict(zip(header, first_half))

        second_half = row[23:]
        second = dict(zip(header, second_half))

        for key in header:
            if key != 'file_id' and key !='id':
                diff.append({
                    key : {
                        'old': first[key],
                        'new': second[key],
                        'date': second['transaction_date'],
                        'changed': True if first[key] != second[key] else False
                    }
                })

        diffs.append(diff)

    diffs = filter(lambda x: x!=[], diffs)

    with open('data/diff.json', 'w') as outfile:
        json.dump(diffs, outfile, indent=2)
