import csv

people_file = open('people.csv')
people_csv = csv.reader(people_file)
for person in people_csv:
    if person[3][0] == 'D':
        print(person[1] + " " + person[0] + " lives in " + person[3])