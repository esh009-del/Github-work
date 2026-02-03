
#opening the file and reading data as before as plain text
# csv_file = open("my_data.csv")
# csv_data = csv_file.read()
# print(csv_data)
# output of code:
# id , name , dept
# 10 , john , hr
# 20, peter , finance


import csv
# #opening file and reading data as list of lists using csv reader
# csv_file = open("my_data.csv")
# csv_data = csv.reader(csv_file)
# csv_lines = list(csv_data)
# for line in csv_lines:
#     print(line)

#output of above code is:
# ['id ', ' name ', ' dept']
# ['10 ', ' john ', ' hr']
# ['20', ' peter ', ' finance']

# csv_file = open("my_data.csv")
# csv_data = csv.DictReader(csv_file)
# csv_lines = list(csv_data)
# #print(csv_lines)
# for line in csv_lines:
#     print(line)

#output of code will be:
#{'id ': '10 ', ' name ': ' john ', ' dept': ' hr'}
#{'id ': '20', ' name ': ' peter ', ' dept': ' finance'}


