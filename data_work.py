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
    whole_2011_list = (csv_read("All_Data_2011.csv"))
    a =[]
    for i in range(92,122):
        a.append(whole_2011_list[i])
    pd = pandas.DataFrame(a)
    pd.to_csv("mosquito_2011_5_bef.csv")

    result_list = []# result
    temp_list = [] # initialize

    humidity = float(whole_2011_list[92][1])+float(whole_2011_list[93][1])
    rainfall = float(whole_2011_list[92][2])+float(whole_2011_list[93][2])
    max_tem = float(whole_2011_list[92][3])+float(whole_2011_list[93][3])
    avg_tem = float(whole_2011_list[92][4])+float(whole_2011_list[93][4])
    min_tem = float(whole_2011_list[92][5])+float(whole_2011_list[93][5])

    temp_list.extend((humidity,rainfall,max_tem,avg_tem,min_tem))
    result_list.append(temp_list)

    for i in range(94, 122):
        temp = list((float(result_list[len(result_list) - 1][0]) + float(whole_2011_list[i][1]),
                         float(result_list[len(result_list) - 1][1]) + float(whole_2011_list[i][2]),
                         float(result_list[len(result_list) - 1][2]) + float(whole_2011_list[i][3]),
                         float(result_list[len(result_list) - 1][3]) + float(whole_2011_list[i][4]),
                         float(result_list[len(result_list) - 1][4]) + float(whole_2011_list[i][5])))
        result_list.append(temp)

    # for item in result_list:
    #     print(item)

    pd=pandas.DataFrame(result_list)
    pd.to_csv("mosquito_2011_5_acu.csv")








