import csv
import sys
import re

data = [] 
file_name = 'Data_Pre_Clean.csv'

with open(file_name,'r') as cfile:
	rows = csv.reader(cfile, delimiter=',')
	for row in rows:
		data.append(row)

#data = [list(x) for x in zip(*data)]            

rem_rows = []
rem_cols = [16,15,6,5,4,3,2,0]
regex = re.compile(r".*(\d{5}(\-\d{4})?)$")

for i in range(1,len(data)):
	if((regex.search(data[i][17])) is None):
		data[i][17] = str(00000)
	if((data[i][6]) in (None,'')):
		rem_rows.append(i)
	if(data[i][7] in (None,'')):
		if(data[i][8] == ''):
			data[i][7] = "DN"
		else:
			data[i][7] = "AP"
	if(len(data[i][9]) == 0):
		data[i][9] = "U"
	if(data[i][10] in (None,'')):
		data[i][10] = "U"
	if(data[i][12] in (None,'')):
		data[i][12] = "U"
	if(data[i][13] in (None,'')):
		data[i][13] = "N"
	if((data[i][14]) in (None,'')):
		rem_rows.append(i)
rem_rows = list(set(rem_rows))
rem_rows.sort(reverse=True)

for k in rem_rows:
	del data[k]
k = 0
data = list(zip(*data))

for k in rem_cols:
	del data[k]

data = list(zip(*data))
with open('Data_Clean.csv', 'w', newline = '') as f:
    writer = csv.writer(f)
    for row in data:
        writer.writerow(row)                        