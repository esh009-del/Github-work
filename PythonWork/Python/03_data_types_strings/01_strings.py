string1="HelloPython"
#remember string index starts from 0
print(string1[2])


print(string1[2:5]) #means do not include 5 only 2  3  4

#instead if you want to include 5 do
print(string1[2:6]) #this will not include 6 
print(string1[7:13])
#if you wnat to start from a certain  number all the way to the end just do this
print(string1[5:])

# if you wnat to start from a certain  number all the way to the start just do this
print(string1[:5])
#if you skip it the entire string will come 
print(string1[:])




#python also includes length of the string 
#string size is denoted by aproperty called length
print(len(string1))
 
#finding the length of the string 
print(string1[len(string1)-10])
#this will give you the first character of the string which is the 1st index
print(string1[len(string1)-1]) 
#this will give you the last character of the string which is the 10th index
print(string1[-1])
#this will also give you the last character of the string which is the 10th index
print(string1[-3])  
#this will give you the 8th character of the string which is the 7th index

print("shush")