import csv

data = []
with open('Data_Mine.csv','r') as cfile:
	rows = csv.reader(cfile, delimiter=',')
	for row in rows:
		data.append(row)

data_exam = []
data_agility = []
data_bg = []
data_interview = []
data_hired = []

data_exam.append(data[0])
data_agility.append(data[0])
data_bg.append(data[0])
data_interview.append(data[0])
data_hired.append(data[0])

#Application Pass
for i in range(1,len(data)):
	if(data[i][6] == 'pass'):
		data_exam.append(data[i])

for i in range(1,len(data)):
	if(data[i][7] == 'pass'):
		data_agility.append(data[i])

for i in range(1,len(data)):
	if(data[i][8] == 'pass'):
		data_bg.append(data[i])

for i in range(1,len(data)):
	if(data[i][9] == 'pass'):
		data_interview.append(data[i])

for i in range(1,len(data)):
	if(data[i][10] == 'pass'):
		data_hired.append(data[i])								                 

with open('Exam_Data.csv', 'w', newline = '') as f:
    writer = csv.writer(f)
    for row in data_exam:
        writer.writerow(row)

with open('Agility_Data.csv', 'w', newline = '') as f:
    writer = csv.writer(f)
    for row in data_agility:
        writer.writerow(row)

with open('BG_Data.csv', 'w', newline = '') as f:
    writer = csv.writer(f)
    for row in data_bg:
        writer.writerow(row)

with open('Interview_Data.csv', 'w', newline = '') as f:
    writer = csv.writer(f)
    for row in data_interview:
        writer.writerow(row)                        

with open('Hired_Data.csv', 'w', newline = '') as f:
    writer = csv.writer(f)
    for row in data_hired:
        writer.writerow(row)