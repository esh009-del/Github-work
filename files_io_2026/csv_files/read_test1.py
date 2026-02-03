
import csv 
with open("my_data.csv") as csv_file:
    csv_data = csv.DictReader(csv_file)
    csv_lines = list(csv_data)
    for line in csv_lines:
        print(line)
    print("inside", csv_file.closed)

print("outside", csv_file.closed)