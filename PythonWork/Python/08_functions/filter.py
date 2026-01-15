numbers=[21,31,1,56, 6 ,99]
# def filter_fucntion(num):
#     return num > 20 
# print(filter_fucntion(10))
# print(filter_fucntion(30))
# filter_function_filter=list(filter(filter_fucntion , numbers))
# print(filter_function_filter)

def odd_filter(numb):
    return numb % 2 != 0 
print(odd_filter(27))
print(odd_filter(16))
filter_odds_function=list(filter(odd_filter, numbers))
print(filter_odds_function)
                          
