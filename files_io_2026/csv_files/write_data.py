import csv
new_data = {"id": 30 , "name" :"harvey" , "dept" :"IT"}
new_data1 = {"id": 30 , "name" :"harvey" , "dept" :"IT"}
new_data2 = {"id": 30 , "name" :"harvey" , "dept" :"IT"}
new_data3 = {"id": 30 , "name" :"harvey" , "dept" :"IT"}

csv_file = open("my_data.csv", "w")
fields= ["id" , "name", "dept"]
writer = csv.DictWriter(csv_file , fieldnames=fields , lineterminator="/n")

writer.writeheader()
writer.writerow(new_data)
writer.writerow(new_data1)
writer.writerow(new_data2)
writer.writerow(new_data3)
csv_file = open("my_data.csv", "a")
fields=list(new_data1.keys())
writer = csv.DictWriter(csv_file , fieldnames=fields , lineterminator="/n")
writer.writerow(new_data2)
writer.writerow(new_data2)
