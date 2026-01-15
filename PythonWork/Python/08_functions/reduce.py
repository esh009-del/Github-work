from functools import reduce

numbers =[1,2,3,4,5,6,7,8,9,10]
# def sum_of_numbers(number1 , number2):
#     return number1 + number2

# # print(sum_of_numbers(90,78))
# results=reduce(sum_of_numbers , numbers)
# print(results)

def max_finder(num1, num2 ):
    if num1 > num2:
        return num1
    else:
       return num2

results = reduce(max_finder , numbers)
print(results)



#modules- way to amke  reuseable code




