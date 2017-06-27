import csv
import math

w1 =  0.0372998
w2 = -0.01532235
w3 = -0.71386385
w4 = -0.18444608
w5 = 1.64801347
b = 1.76021981

def listTofloat(factor):
    newList = []
    for i in range((len(factor))):
        newList.append(float(factor[i][0]))
    return newList

def changeToLevel(list):
    level=[]
    for i in range(len(list)):
        if(0<=list[i]<21):
            level.append("1")
        elif(21<=list[i]<41):
            level.append("2")
        elif (41 <= list[i] <81):
            level.append("3")
        elif (81 <= list[i] < 161):
            level.append("4")
        elif (161 <= list[i] < 321):
            level.append("5")
        elif (321 <= list[i] <641):
            level.append("6")
        elif (641 <= list[i] < 1281):
            level.append("7")
        elif (list[i]>=1281):
            level.append("8")
        else:
            level.append("1") # <0 is predicting level 1

    return level

def changeToLevelLog(list):
    logScale = []
    for i in range(len(list)):
        if(list[i]<=20):
            logScale.append("1")
        else:
            logScale.append(math.ceil(math.log(list[i]/10,10)))

    return logScale

if __name__ == '__main__':
    with open('mosquito_result_test.csv', 'r', errors='ignore') as f:
        reader = csv.reader(f, delimiter=',')
        included_cols = [0, 1, 2, 3, 4, 5]
        testHumidity = []
        testRainfall = []
        testMaxTem = []
        testAvgTem = []
        testMinTem = []
        testCatchMosquito = []
        for row in reader:
            content = list(row[i] for i in included_cols)
            testHumidity.append((content[0].split('\n')))
            testRainfall.append(content[1].split('\n'))
            testMaxTem.append(content[2].split('\n'))
            testAvgTem.append(content[3].split('\n'))
            testMinTem.append(content[4].split('\n'))
            testCatchMosquito.append(content[5].split('\n'))

    testHumidity = listTofloat(testHumidity)
    testRainfall = listTofloat(testRainfall)
    testMaxTem = listTofloat(testMaxTem)


    testAvgTem = listTofloat(testAvgTem)
    testMinTem = listTofloat(testMinTem)
    testCatchMosquito = listTofloat(testCatchMosquito)

    mosquito_result = []

    for i in range(len(testCatchMosquito)):
        mosquito_result.append(w1 * testHumidity[i] + w2 * testRainfall[i] + w3 * testMaxTem[i] + w4 * testAvgTem[i] + w5 *testMinTem[i] + b)

    print (mosquito_result)

    mosquito_result = changeToLevelLog(mosquito_result)
    testCatchMosquito = changeToLevelLog(testCatchMosquito)

    print ((mosquito_result))
    print ((testCatchMosquito))

    cnt = 0
    for i in range(len(mosquito_result)):
        if(abs(int(mosquito_result[i])-int(testCatchMosquito[i]))==0):
            cnt += 1

    print (cnt/len(mosquito_result)*100)

    #No log scale -> 46.9% Yes log Scale -> 93% abs(x-y) <= 1
    #No log scale -> 18.3% Yes log Scale -> 45.6% Just same case





