import csv

def csv_read(file):
     raw_data = []
     with open(file,"r") as datafile:
         reader = csv.reader(datafile,delimiter=',')
         for row in reader:
             raw_data.append(row)

     return raw_data

def make_dictionary(f_list):
    factor_dictionary =dict()
    for i in range(len(f_list)):
        factor_dictionary[f_list[i][0]]=f_list[i][1:len(f_list[i])]

    return factor_dictionary

if __name__ == '__main__':
    print(make_dictionary(csv_read("All_Data_2011.csv")))
