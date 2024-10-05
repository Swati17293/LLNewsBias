import csv
import os

list_file = ['d2019','d2020','d2021','d2022']

for fl in list_file:
    os.mkdir(f'data/{fl}/')

csv_file = open(f'data/d2019/d2019.csv','a',newline='\n') 
csv_writer_d2019 = csv.writer(csv_file, delimiter=',')  

csv_file = open(f'data/d2020/d2020.csv','a',newline='\n') 
csv_writer_d2020 = csv.writer(csv_file, delimiter=',')

csv_file = open(f'data/d2021/d2021.csv','a',newline='\n') 
csv_writer_d2021 = csv.writer(csv_file, delimiter=',')

csv_file = open(f'data/d2022/d2022.csv','a',newline='\n') 
csv_writer_d2022 = csv.writer(csv_file, delimiter=',')

csv_file = open(f'data/2022.csv','r',newline='\n') 
csv_reader = csv.reader(csv_file, delimiter=',')
    
for row in csv_reader:
    x = row[4].split('-')[0]
    
    if x == '2019': 
        csv_writer_d2019.writerow(row)
    elif x == '2020':
        csv_writer_d2020.writerow(row)
    elif x == '2021':
        csv_writer_d2021.writerow(row)
    elif x == '2022':
        csv_writer_d2022.writerow(row)