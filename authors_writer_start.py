field_names = ['First Name', 'Last Name', 'Email', 'Date of Birth']
authors_list = [['Jeromy', 'Tremblay', 'lemke.dahlia@example.com', '1984-12-27'],
                ['Erna', 'Konopelski', 'volkman.johnathan@example.com', '1988-04-27'],
                ['Giuseppe', 'Schulist', 'armstrong.adonis@example.net', '1970-06-03'],
                ['Bobby', 'Cormier', 'cassin.conor@example.net', '1971-05-13'],
                ['Breanne', 'Zieme', 'emard.jacklyn@example.com', '2020-01-30'],
                ['Charlene', 'Dicki', 'maggio.noemy@example.org', '1995-04-21']]
with open('authors_out.csv', 'w') as authors_out_file:
    for row in authors_list:
        authors_out_file.write(str(row)+'\n')
