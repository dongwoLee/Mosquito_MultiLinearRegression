import csv
import tensorflow as tf
import math
import numpy as np
import pandas as pd

def listTofloat(factor):
    newList = []
    for i in range((len(factor))):
        newList.append(float(factor[i][0]))
    return newList

def adaptLog(list):
    logScale = []
    for i in range(len(list)):
        if (list[i] <= 20):
            logScale.append("1")
        else:
            overEight = (math.ceil(math.log(list[i] / 10, 2)))
            if (overEight >= 8):
                logScale.append("8")
            else:
                logScale.append(str(overEight))

    return logScale

if __name__ == '__main__':
    with open('training_data_again.csv', 'r', errors='ignore') as f:
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
    catchMosquito = adaptLog(listTofloat(catchMosquito))
    catchMosquito = list(map(float,catchMosquito))

    W1 = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
    W2 = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
    W3 = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
    W4 = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
    W5 = tf.Variable(tf.random_uniform([1], -1.0, 1.0))

    b = tf.Variable(tf.random_uniform([1], -1.0, 1.0))

    hypothesis = W1 * humidity + W2 * rainfall + W3 * maxTem + W4 * avgTem + W5 * minTem + b

    cost = tf.reduce_mean(tf.square(hypothesis-catchMosquito))

    optimizer = tf.train.AdamOptimizer(learning_rate=(1e-5))
    train = optimizer.minimize(cost)

    init = tf.global_variables_initializer()
    sess = tf.Session()
    sess.run(init)

    for step in range(100001):
        sess.run(train)
        if step % 1000 == 0:
            print(step, sess.run(cost), sess.run(W1), sess.run(W2), sess.run(W3), sess.run(W4), sess.run(W5), sess.run(b))

