import csv
from datetime import datetime

data = [] 

file_name = 'Data_Clean_Final.csv'
with open(file_name,'r') as cfile:
	rows = csv.reader(cfile, delimiter=',')
	for row in rows:
		data.append(row)

def days_between(d1, d2):
	d1 = datetime.strptime(d1, "%d-%m-%Y")
	d2 = datetime.strptime(d2, "%d-%m-%Y")
	days = abs((d2 - d1).days)
	year = int(days/365)
	return(year)

for i in range(1,len(data)):
	if(not(str(data[i][0]) and str(data[i][5]))):	
		data[i].append(str(0))
	else:		
		age = days_between(data[i][0],data[i][5])
		data[i].append(str(age))

data[0].append('Age')
with open('Data_Clean_F.csv', 'w', newline = '') as f:
    writer = csv.writer(f)
    for row in data:
        writer.writerow(row)