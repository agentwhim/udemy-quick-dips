people_file = open('people.csv')
for line in people_file:
    print(line[:-1])