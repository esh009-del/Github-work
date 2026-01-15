string1 ="hello"
print(string1.capitalize())
print(string1)

#Wont change string1 because strings are immutable
string1 = string1.capitalize()
print(string1)
#Will change string1 because we reassigned it to the capitalized version of itself
#print(string1)

#new examople
player_details_list={ "name": "john", "age":  25, "height": 6.5, "profession": "Basketball"}

print(player_details_list["name"])
print(player_details_list["age"])       
print(player_details_list["height"])
print(player_details_list["profession"])
ordering ={
     1:"one",
     2:"two"
 }
print(ordering[1])

mixed_dict={
    True:"bool key",
    False:"bool value"
}
print(mixed_dict[True])
print("shush")