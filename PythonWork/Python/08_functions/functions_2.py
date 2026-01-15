def greet():
  print("Hello")
    

input_no=int(input("enter no of students"))
def calculate_average(marks):
    if not marks:
        print("No marks provided.")
        return
    total = sum(marks)   
    average= total/len(marks)
    print("Average marks:", average)
marks=[]

for i  in range(input_no):
    marks.append(int(input("enter marks")))

calculate_average(marks)

#calculate average
print("shush")