import csv
import math

w1 =0.00264151
w2 = -0.00375117
w3 = -0.25488108
w4 = 0.54489952
w5 = -0.28670394
b = 0.88455576

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
    with open('test_data_again.csv', 'r', errors='ignore') as f:
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

    # for i in range(len(mosquito_result)):
    #     mosquito_result[i] = math.ceil(mosquito_result[i])
    #     if(mosquito_result[i]>8):
    #         mosquito_result[i]=8
    #     elif(mosquito_result[i]<1):
    #         mosquito_result[i]=1
    # print (mosquito_result)

    # mosquito_result = list(map(int,mosquito_result))
    # for i in range(len(mosquito_result)):
    #     if(mosquito_result[i]<=0):
    #         mosquito_result[i] = 1
    #     elif(mosquito_result[i]>=8):
    #         mosquito_result[i]=8
    #
    # print (mosquito_result)
    # cnt = 0
    # for i in range(len(mosquito_result)):
    #     if(abs(int(mosquito_result[i])-int(testCatchMosquito[i]))<=1):
    #         cnt += 1
    #
    # print (cnt/len(mosquito_result)*100)






