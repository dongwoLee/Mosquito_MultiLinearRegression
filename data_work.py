import csv
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


