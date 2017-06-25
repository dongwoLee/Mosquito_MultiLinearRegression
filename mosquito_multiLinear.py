import csv
import tensorflow as tf
import numpy as np
import pandas as pd

with open('mosquito_result_training.csv','r') as f:
    reader = csv.reader(f,delimiter=',')
    included_cols = [0,1,2,3,4,5]
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


