import csv
import os

list_file = ['brexit','covid','election','uarowar']

for fl in list_file:

    csv_file = open(f'data/{fl}.csv','r',newline='\n') 
    csv_reader = csv.reader(csv_file, delimiter=',')

    os.mkdir(f'data/{fl}/')

    csv_file = open(f'data/{fl}/{fl}.csv','a',newline='\n') 
    csv_writer = csv.writer(csv_file, delimiter=',')

    list_ = []

    for row in csv_reader:
        if row[5] in list_:
            pass
        else:
            x = row[5].split(' ')
            if len(x) > 4: 
                list_.append(row[5])
                csv_writer.writerow(row)