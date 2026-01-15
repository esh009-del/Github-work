print("hi world")
name=input("What is your name?")



#lambda function

circ= lambda side1 , side2 , side3: side1 + side2 + side3
print(circ(2,3,4))

def circ(side1 , side2 , side3):
    return side1 + side2 + side3

circ= lambda side1 , side2 , side3: side1 + side2 + side3
print(circ(2,3,4))



## new page ####
#we have a list of numbers
#we want to get a list with eaqch number squared

numbers = [1, 2 , 3 , 4 , 5]
squared_numbers= []
# for number in numbers:
#     squared_numbers.append(number **2)

for number in numbers:
    squared_numbers.append(number **2)
    print(squared_numbers)  

numbers=[1,2,3,4,5] #input list of numbers
def square_the_number(num): #
    return num **2
square_of_7=square_the_number(7) 
print(square_of_7)

squares=[]

for i in numbers:
    # print(square_the_number(i))
    squares.append(square_the_number(i))
print(squares)
 
numbers=[1,2,3,4,5] #input list of numbers
def square_the_number(num): #
    return num **2

squares=list(map(square_the_number, numbers))
print(squares)

squares_map=map(square_the_number, numbers)
squares_list=list(squares_map)
print(squares_list)

print("shush")