# numbers = [1,2,3,4,5,6,7]
# def triple_the_number(num):
#     return num * 3 
# ANSWER = triple_the_number(2) 
# print(ANSWER)

# triple_list=list(map(triple_the_number , numbers ))
# print(triple_list) 
# map accepts two values which are function name  and list
names =["Neel" , "Aryan" , "Vimush" , "Eshaan" , "Akira"]
def convert_uppercase(name):
    return name.upper()
answer = convert_uppercase("Neel")
print(answer)
convert_uppercase_map=list(map(convert_uppercase, names))
print(convert_uppercase_map)
filter()