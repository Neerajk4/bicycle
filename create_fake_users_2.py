import random
import sys
from faker import Faker
from bootstrap_table import db, User3
import pandas as pd

#User2.__table__.drop(db.engine)
#User2.__table__.drop(db.engine)
#print(db.Model.table_names())

df = pd.read_csv("static/results.csv")
#print(len(df))

"""
for ind in df.index:
    print(type(df['Date'][ind]))
    print(type(df['Vikram'][ind]))
    print(type(df['Neeraj'][ind]))
    print(type(df['Link'][ind]))
    print(type(df['Headline'][ind]))
    user = User3(date1=df['Date'][ind],
                vikram=int(df['Vikram'][ind]),
                neeraj=int(df['Neeraj'][ind]),
                link=df['Link'][ind],
                headline=df['Headline'][ind])
    db.session.add(user)
    db.session.commit()
    ind = ind + 1
print(f'Added {ind} records to the database.')

"""
def query_results():
    users = User3.query
    for user in users:
        print(user.date1)
        print(user.vikram)
        print(user.neeraj)
        print(user.link)
        print(user.headline)

query_results()

