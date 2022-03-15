import csv

field_names = ['First Name', 'Last Name', 'Email', 'Date of Birth']
authors_list = [['Jeromy', 'Tremblay', 'lemke.dahlia@example.com', '1984-12-27'],
                ['Erna', 'Konopelski', 'volkman.johnathan@example.com', '1988-04-27'],
                ['Giuseppe', 'Schulist', 'armstrong.adonis@example.net', '1970-06-03'],
                ['Bobby', 'Cormier', 'cassin.conor@example.net', '1971-05-13'],
                ['Breanne', 'Zieme', 'emard.jacklyn@example.com', '2020-01-30'],
                ['Charlene', 'Dicki', 'maggio.noemy@example.org', '1995-04-21']]
with open('authors_out.csv', 'w', newline='') as authors_out_file:
    authors_csv = csv.DictWriter(authors_out_file, field_names)
    authors_csv.writeheader()
    for row in authors_list:
        author = {field_names[index]: value for index, value in enumerate(row)}
        authors_csv.writerow(author)
        