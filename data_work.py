import csv
import pandas
import operator
import collections

#humidity,rainfall,tem_max,tem_avg,tem_min,mosquito

def csv_read(file):
     raw_data = []
     with open(file,"r") as datafile:
         reader = csv.reader(datafile,delimiter=',')
         for row in reader:
             raw_data.append(row)

     return raw_data

if __name__ == '__main__':
    # 2011.05.02 idx = 121
    #whole_2011_list = (csv_read("All_Data_2011.csv"))
    #whole_2012_list = (csv_read("All_Data_2012.csv"))
    #whole_2013_list = (csv_read("All_Data_2013.csv"))
    whole_2014_list = (csv_read("All_Data_2014.csv"))
    a =[]
    for j in range(212,243):
        for i in range(j-29,j):
            a.append(whole_2014_list[i])
        pd = pandas.DataFrame(a)
        pd.to_csv("mosquito_2011_5_bef.csv",sep=',',encoding='utf-8')

    result_list = []# result
    temp_list = [] # initialize

    for i in range(212,243):
        temp_list = []  # initialize
        humidity = float(whole_2014_list[i-1][1])+float(whole_2014_list[i-2][1])
        rainfall = float(whole_2014_list[i-1][2])+float(whole_2014_list[i-2][2])
        max_temp = float(whole_2014_list[i-1][3])+float(whole_2014_list[i-2][3])
        avg_temp = float(whole_2014_list[i-1][4])+float(whole_2014_list[i-2][4])
        min_temp = float(whole_2014_list[i-1][5])+float(whole_2014_list[i-2][5])

        temp_list.extend((humidity,rainfall,max_temp,avg_temp,min_temp))
        result_list.append(temp_list)

        for j in range(i-3, i-31,-1):
            temp = list((float(result_list[len(result_list) - 1][0]) + float(whole_2014_list[j][1]),
                             float(result_list[len(result_list) - 1][1]) + float(whole_2014_list[j][2]),
                             float(result_list[len(result_list) - 1][2]) + float(whole_2014_list[j][3]),
                             float(result_list[len(result_list) - 1][3]) + float(whole_2014_list[j][4]),
                             float(result_list[len(result_list) - 1][4]) + float(whole_2014_list[j][5])))
            result_list.append(temp)

        # for item in result_list:
        #     print(item)

        df=pandas.DataFrame(result_list)
        df.to_csv("mosquito_2011_5_acu.csv",sep=',',encoding='utf-8')










