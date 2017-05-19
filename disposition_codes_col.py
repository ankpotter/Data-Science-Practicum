import csv
import sys
import re

data = [] 

file_name = 'Data_Clean.csv'
with open(file_name,'r') as cfile:
	rows = csv.reader(cfile, delimiter=',')
	for row in rows:
		data.append(row)
codes = []

with open('Book1.csv','r') as cfile:
	rows = csv.reader(cfile, delimiter=',')
	for row in rows:
		codes.append(row)		

d_code = {}

for i in codes:
	d_code[i[0]] = ":".join(i[1:7]) 


del_rows = []

for i in range(1,len(data)):
	if(data[i][-2] == 'TR'):
		del_rows.append(i)	
	else:
		value = d_code[data[i][-2]]
		state = value.split(':')
		data[i].extend(state)

data[0].extend(['Application','Exam','Agility','Background','Interview','Hired'])

del_rows = list(set(del_rows))
del_rows.sort(reverse=True)

for k in del_rows:
	del data[k]

with open('Data_Clean_Final.csv', 'w', newline = '') as f:
    writer = csv.writer(f)
    for row in data:
        writer.writerow(row)                        