import csv
import datetime

with open('authors.csv') as authors_file:
    authors_reader = csv.DictReader(authors_file)
    authors = {row['First Name']+' '+row['Last Name']: datetime.date.fromisoformat(row['Date of Birth'])
               for row in authors_reader if row['DateTime Added'][:4] == '2019'}
    print(authors)