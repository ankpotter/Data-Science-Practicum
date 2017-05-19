import csv
import itertools

file_name = 'applicantdata.csv'
file_name_2 = 'PoliceRecruits.csv'

data = []
with open(file_name,'r') as cfile:
	rows = csv.reader(cfile, delimiter=',')
	for row in rows:
		data.append(row)

data2 = []
with open(file_name_2,'r') as cfile:
	rows = csv.reader(cfile, delimiter=',')
	for row in rows:
		data2.append(row)


data = [list(x) for x in zip(*data)]            
data2 = [list(x) for x in zip(*data2)]
k =[1,5,12,9,10,11,8,13,14]

print(len(data[1]))
for i in range(9):
	data[k[i]].extend(data2[i])

data = list(itertools.zip_longest(*data,fillvalue='null'))

with open('Data_Pre_Clean.csv', 'w', newline = '') as f:
    writer = csv.writer(f)
    for row in data:
        writer.writerow(row)	