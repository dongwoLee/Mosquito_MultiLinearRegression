import csv
import math

w1 = 0.00166559
w2 = -0.00320032
w3 = -0.00170021
w4 = -0.02722645
w5 = 0.0364294
b = 1.27694166

def listTofloat(factor):
    newList = []
    for i in range((len(factor))):
        newList.append(float(factor[i][0]))
    return newList

def changeToLevelLog(list):
    logScale = []
    for i in range(len(list)):
        if(list[i]<=20):
            logScale.append("1")
        else:
            overEight = (math.ceil(math.log(list[i] / 10, 2)))
            if(overEight>=8):
                logScale.append("8")
            else:
                logScale.append(str(overEight))

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
    testCatchMosquito = changeToLevelLog(listTofloat(testCatchMosquito))
    testCatchMosquito = list(map(int,testCatchMosquito))

    print (testCatchMosquito)

    mosquito_result = []

    for i in range(len(testCatchMosquito)):
        mosquito_result.append(w1 * testHumidity[i] + w2 * testRainfall[i] + w3 * testMaxTem[i] + w4 * testAvgTem[i] + w5 *testMinTem[i] + b)

    cnt = 0
    for i in range(len(mosquito_result)):
        if(abs(int(mosquito_result[i])-int(testCatchMosquito[i]))==0 or int(mosquito_result[i])-int(testCatchMosquito[i])==1):
            cnt += 1

    print (cnt/len(mosquito_result)*100)






