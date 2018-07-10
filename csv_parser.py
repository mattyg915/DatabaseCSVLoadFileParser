import csv

ids_to_keep = []
new_list = []

i = 0

with open('origin_table.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in reader:
        id_one = row[0]
        actor_id = row[1]
        ids_to_keep.append(id_one)
        actors_to_keep.append(actor_id)

with open('origin_table.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in reader:
        id_two = row[1]
        if id_two in ids_to_keep:
            new_list.append(row[1] + "," + row[2])

import_file = open("classifies_table.csv", "w")

for item in new_list:
    import_file.write(item + "\r")

import_file.close()
