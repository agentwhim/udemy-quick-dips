import csv
cities_list = [[6, 'Rigomagus', 'Remagen', 'Germany'],
    [6, 'Aquae Mattiacorum', 'Wiesbaden', 'Germany'],
    [9, 'Mursa', 'Osijek', 'Croatia'],
    [15, 'Emona', 'Ljubljana', 'Slovenia'],
    [15, 'Vindonissa', 'Windisch', 'Switzerland'],
    [41, 'Lugdunum Batavorum', 'Katwijk', 'Netherlands'],
    [42, 'Aequum', 'Citluk', 'Croatia'],
    [43, 'Londinium', 'London', 'UK'],
    [43, 'Albanianis', 'Alphen aan den Rijn', 'Netherlands'],
    [43, 'Lauri', 'Woerden', 'Netherlands']]
cities_file = open('cities.csv', 'w', newline='')
cities_writer = csv.writer(cities_file)
for city in cities_list:
    cities_writer.writerow(city)
cities_file.close()