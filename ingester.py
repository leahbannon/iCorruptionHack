"""
Push new data to sqlite database.
"""
import dateutil.parser
import datetime

from peewee import *

from models.Contribution import Contribution

db = SqliteDatabase('contributions.db')

def parse_fec_file(infile):
    f = open(infile)
    res = []
    for line in f:
        res.append(parse_line(line))
    return [line_to_dict(val) for val in res]

def parse_line(l):
    vals = l.split('|')
    vals = map(lambda x:None if x=='' else x,vals)
    int_cols = [18-1,21-1] #file num and sub id
    for i in int_cols:
        if vals[i] is not None:
            vals[i] = int(vals[i])
    float_cols = [15-1] #transaction amount
    for i in float_cols:
        if vals[i] is not None:
            vals[i] = float(vals[i])
    date_cols = [14-1] #date
    for i in date_cols:
        vl = vals[i]
        if vl is not None:
            vals[i] = datetime.datetime(month=int(vl[0:2]), day=int(vl[2:4]), year=int(vl[4:8]))
    return vals

def line_to_dict(row):
    return {
        "comittee_id" : row[0],
        "ammendment_id" : row[1],
        "report_type" : row[2],
        "transaction_pgi" : row[3],
        "image_num" : row[4],
        "transaction_tp" : row[5],
        "entity_tp" : row[6],
        "name" : row[7],
        "city" : row[8],
        "state" : row[9],
        "zip_code" : row[10],
        "employer" : row[11],
        "occupation" : row[12],
        "transaction_date" : row[13],
        "transaction_amount" : str(row[14]),
        "other_id" : row[15],
        "transaction_id" : row[16],
        "file_num" : row[17],
        "memo_cd" : row[18],
        "memo_text" : row[19],
        "sub_id" : row[20]
    }

def ingested(infile):
    '''Return true if file is already ingested, false otherwise'''
    pass

def ingest(filepath):
    '''Ingest file into sqlite database'''
    rows = parse_fec_file(filepath)
    # Fastest.
    with db.transaction():
        for idx in range(0, len(rows), 500):
            print "Inserting row %d of %s" % (idx, filepath)
            Contribution.insert_many(rows[idx:idx+500]).execute()

    # with db.transaction():
    #     Contribution.insert_many(rows).execute()

if __name__ == '__main__':
    # ingest files
    filepath = "data/FEC 2014 2.17.2014/itcont.txt"
    # items = ingest(filepath)
    ingest(filepath)
    # ['C00162578', 'N', 'M3', None, '13961173948', '15', 'IND', 'WILLIS-MILLER, TAUNJA', 'CHARLESTON', 'WV', '25304', 'JACKSON & KELLY', 'ATTORNEY', datetime.datetime(2013, 2, 22, 0, 0), 1000, None, '11AI-000021126', 861004, None, None, 4031820131185265954]

# ['C00162578'
#  'N'
#  'M3'
#  None
#  '13961173948'
#  '15'
#  'IND'
#  'WILLIS-MILLER
#  TAUNJA'
#  'CHARLESTON'
#  'WV'
#  '25304'
#  'JACKSON & KELLY'
#  'ATTORNEY'
#  datetime.datetime(2013, 2, 22, 0, 0)
#  1000
#  None
#  '11AI-000021126'
#  861004
#  None
#  None
#  4031820131185265954]

