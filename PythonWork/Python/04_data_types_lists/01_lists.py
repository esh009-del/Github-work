player_details=["jordan" ,25 ,"USA"]
additional_details=["6ft6in" ,"chicago"]
print(player_details)
print(type(player_details))
#is a list
print(player_details[0]) #accessing first element
print(player_details[1]) #accessing second element
print(player_details[2]) #accessing third element

print(player_details*3) # Will repeat the list 3 times
print(player_details + additional_details) # Will concatenate two lists
player_details[1]=26 #modifying second element
print(player_details)
print("shush")
