import csv
import os
import pandas as pd

# dataset order for text classification (event-wise)
order_event= {
    1: ['brexit', 'covid', 'election', 'uarowar'],
    2: ['election','covid', 'uarowar', 'brexit'],
    3: ['brexit', 'uarowar', 'election', 'covid'],
    4: ['covid', 'brexit', 'uarowar', 'election']
}

# dataset order for text classification (year-wise)
order_year = {
    1: ['d2019', 'd2020', 'd2021', 'd2022'],
    2: ['d2021','d2020', 'd2022', 'd2019'],
    3: ['d2019', 'd2022', 'd2021', 'd2020'],
    4: ['d2020', 'd2019', 'd2022', 'd2021']
}
 
def create_ordered_test_data(c_type):

    list_file = []

    if c_type == 'event':
        list_file = ['brexit','covid','election','uarowar']

    if c_type == 'year':
        list_file = ['d2019','d2020','d2021','d2022']

    if os.path.exists(f'data/{c_type}/') == False:
        os.mkdir(f'data/{c_type}/')

    csv_file_w = open(f'data/{c_type}/test_tmp.csv','a',newline='\n') 
    csv_writer = csv.writer(csv_file_w, delimiter=',')  

    for fl in list_file:
        
        csv_file_r = open(f'data/{fl}/test.csv','r',newline='\n') 
        csv_reader = csv.reader(csv_file_r, delimiter=',')

        for row in csv_reader:
            csv_writer.writerow(row)
            
    df = pd.read_csv(f'data/{c_type}/test_tmp.csv', header=None, delimiter=',')  
    shuffled_df = df.sample(frac=1.0, ignore_index=True).reset_index(drop=True)
    shuffled_df.to_csv(f'data/{c_type}/test.csv', index=False, header=False)

    os.remove(f'data/{c_type}/test_tmp.csv')


def create_ordered_train_data(order,c_type):
    
    list_file = []

    if c_type == 'event':
        list_file = ['brexit','covid','election','uarowar']

    if c_type == 'year':
        list_file = ['d2019','d2020','d2021','d2022']

    if os.path.exists(f'data/{c_type}/') == False:
        os.mkdir(f'data/{c_type}/')

    csv_file_w = open(f'data/{c_type}/train_{order}.csv','a',newline='\n') 
    csv_writer = csv.writer(csv_file_w, delimiter=',')

    for fl in list_file:
        csv_file_r = open(f'data/{fl}/train.csv','r',newline='\n') 
        csv_reader = csv.reader(csv_file_r, delimiter=',')

        for row in csv_reader:
            csv_writer.writerow(row)

def main():

    # create ordered dataset
    total_order = 4

    # classification type
    c_type = ['event','year']

    # create train data
    for _type in c_type:
        for i in range(0,4):
            create_ordered_train_data(str(i+1), _type)
            print("\nTrain data generation complete for order {}".format(i+1))
        
        print(f"\nTrain data generation complete for c_type {_type}")

        # create test data
        create_ordered_test_data(_type)
        print(f"\nTest data generation complete for c_type {_type}")

    print("\nOrdered dataset generation complete\n")


if __name__ == "__main__":
    main()