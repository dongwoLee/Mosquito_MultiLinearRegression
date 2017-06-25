import csv
import tensorflow as tf
import numpy as np
import pandas as pd

def listTofloat(factor):
    newList = []
    for i in range((len(factor))):
        newList.append(float(factor[i][0]))
    return newList

if __name__ == '__main__':
    with open('mosquito_result_training.csv', 'r', errors='ignore') as f:
        reader = csv.reader(f, delimiter=',')
        included_cols = [0, 1, 2, 3, 4, 5]
        humidity = []
        rainfall = []
        maxTem = []
        avgTem = []
        minTem = []
        catchMosquito = []
        for row in reader:
            content = list(row[i] for i in included_cols)
            humidity.append((content[0].split('\n')))
            rainfall.append(content[1].split('\n'))
            maxTem.append(content[2].split('\n'))
            avgTem.append(content[3].split('\n'))
            minTem.append(content[4].split('\n'))
            catchMosquito.append(content[5].split('\n'))

    humidity = listTofloat(humidity)
    rainfall = listTofloat(rainfall)
    maxTem = listTofloat(maxTem)
    avgTem = listTofloat(avgTem)
    minTem = listTofloat(minTem)
    catchMosquito = listTofloat(catchMosquito)

