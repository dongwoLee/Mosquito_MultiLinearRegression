import csv

w1 = 0.00467562
w2 = 0.01372897
w3 = 2.76661563
w4 = -7.44979143
w5 = 5.42038155
b = 10.81032372

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
            level.append("1") # <0 is predicting level 0

    return level

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

    mosquito_result = changeToLevel(mosquito_result)
    testCatchMosquito = changeToLevel(testCatchMosquito)

    cnt = 0
    for i in range(len(mosquito_result)):
        if(abs(int(mosquito_result[i])-int(testCatchMosquito[i]))<=1):
            cnt += 1

    print (cnt/len(mosquito_result)*100)




