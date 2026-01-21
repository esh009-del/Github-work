file_handle = open("C:\\Users\\eshaa\\OneDrive\\Documents\\myfile.txt", "r")
# #have to double \\-->whever we are speicifying windows files into python we have to change sings slash (\) into double slash(\\) 
# # why? because single back slash is used as an escape charctrer in python
# file_data =(file_handle.read())
# print(type(file_data))
# # if we want the next line to work then we have to comment the top part 
# #why?the fike pointer has been placed at the end of the file 
# #this is after we called the .read() function
# # how to fix it
# #use seek function
# file_handle.seek(0)
# line1=file_handle.readline()
# print(line1)

lines=file_handle.readlines()
print(lines)
print(file_handle.closed) #checks if file is closed
file_handle.close()
print(file_handle.closed)
