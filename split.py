from sklearn.model_selection import train_test_split
import pandas as pd
import os
import csv

list_file = ['brexit','covid','election','uarowar']
# list_file = ['d2019','d2020','d2021','d2022']

colnames = ['outlet','bias','id','lang','date','title_ml','category']

for fl in list_file:

    data = pd.read_csv(f'data/{fl}/{fl}.csv', names=colnames, sep=',')

    features = data.drop('bias', axis=1)
    categories = data.bias

    A,B, a,b = train_test_split(features,categories,test_size=0.1, random_state = 0, stratify=categories, shuffle=True)

    test = pd.concat([B, b], axis=1, join='inner')
    train = pd.concat([A, a], axis=1, join='inner')

    test.to_csv(f'data/{fl}/test.csv', sep=',', index=False, header=False)
    train.to_csv(f'data/{fl}/train.csv', sep=',', index=False, header=False)