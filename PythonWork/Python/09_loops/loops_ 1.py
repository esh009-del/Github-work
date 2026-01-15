numbers=[1,2,3,4]
for num in numbers:
    print(num)

for val in range(1,22):
    print(val)
    #Does not include 22

for val in range(5):
    print(val)
    #Starts from 0 and goes to 4
for val in range(2,11,2):
    print(val)
    #Starts from 2 and goes to 10 with a step of 2

for val in range(10,0,-1):
    print(val)
    #Counts backwards from 10 to 1  

for val in range(1,6):
    print(val)
else: 
    print("Loop completed")
    #Executes after the loop is finished normally

NUMBERS = [10, 20, 30, 40, 50]
for num in NUMBERS:
    if num % 2==0:
         print("Found EVEN",num, "stopping the loop.")
         break
         print(num)

numbers=[1, 3, 5, 7, 8, 9]
for num in numbers:
    if num % 2 == 0:
         print("Found EVEN",num)
         print("Found odd",num)
    else:      
     print(num)
 

name="john"
age=25
print(name +" is a good boy")
print("He is "+ str(age) + " years old")
print("{} is a good boy".format(name))
print(f"{name} is a good boy  and he is {age} years old ")
numbers=[1,2,3,4,5]
even_list= []
for num in numbers:
    if num % 2 !=0:
       continue
    even_list.append(num)
print(even_list)
print("shush")