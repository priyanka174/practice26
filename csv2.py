#read data from csv

'''import csv
f=open('H:\\data1.csv')
csv_data=csv.reader(f)
list1=list(csv_data)
print(list1)'''

# read all data from csv
'''import csv
f=open('H:\\data1.csv')
csv_data=csv.reader(f)
list1=list(csv_data)
for row in list1:
    l=len(row)
    for j in range(0,l):
        print(row[j])'''

# write data to csv

import csv
f=open("H:\\write1.csv",'w',newline='')
csv_w=csv.writer(f)
csv_w.writerow(['hello',2,34])
csv_w.writerow(['hdf',2,54])
f.close()