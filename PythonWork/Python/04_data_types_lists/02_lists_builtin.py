#print(dir(list))

"append", "clear", "copy", "count", "extend", "index", "insert", "pop", "remove", "reverse", "sort"

list_ops1=["append", "clear", "copy", "count", "extend", "index", "insert"]
list_ops2=["remove", "reverse", "sort"]

print(list_ops1)
list_ops1.append("pop")
print(list_ops1)
# list_ops1.clear() #clears the list
print(list_ops1)

list1=[1,2,3,4,67,89]
print(list1)
# list1.clear()
print("List after clear:")
print(list1)

print(list1.count(1))#counts occurrences of 1 in the list
#make sure the .clear() line is commented before running this

list_ops1.extend(list_ops2)
print(list_ops1) #first element gets modified
print(list_ops2) #second element remains same
#same thign make sure the .clear() line is commented before runnin this

print(list_ops1.index("extend"))    #index of the first occurrence of "extend"
#remember index start from value 0
list_ops1.insert(2,"new_item")  #inserts "new_item" at index 2
print(list_ops1)

popped_item=list_ops1.pop()  #removes and returns the last item by default
print("Popped item:",popped_item)
# if you want to pop item from a specific index, you can provide the index as an argument to pop() method
# e.g., list_ops1.pop(2) will remove and return the item at index 2
print(list_ops1)

list_ops1.remove("new_item")  #removes the first occurrence of "new_item"
print(list_ops1)
# doesnt return the value removed
list_ops1.reverse()  #reverses the list in place
print(list_ops1)
list_ops1.sort()  #sorts the list in place
print(list_ops1)
# so in alphabetical order
# for numbers it will be in ascending order
# for descending order use sort(reverse=True)
list_numbers=[5,2,9,1,5,6]
list_numbers.sort()
print(list_numbers)
list_numbers.sort(reverse=True)
print(list_numbers)

student=["Ab", 17, "B", "teacher"]
student_copy=student.copy() #creates a shallow copy of the list
print(student)
print(student_copy)
student.clear() #clears the original list
print("Original list after clear:",student)
#shallow copy remains unchanged
print("Shallow copy of the list:",student_copy)
# it is like another variable pointing to the same list in memory but wont be affected if the original list is cleared

# print(student[-1][1])
#shows error as i cleared student list above # also jams the program

#but my shallow copy was unaffected so i can use this fucntionality on student_copy
print(student_copy[1])
#print out the 1st index also known as 2nd value
# prints 20

from copy import deepcopy
student_copy_deep=deepcopy(student_copy) #creates a deep copy of the list
print("Deep copy of the list:",student_copy_deep)
student_copy.clear() #clears the shallow copy
print("Shallow copy after clear:",student_copy)
print("Deep copy remains unchanged:",student_copy_deep)
# deep copy remains unchanged even if shallow copy is cleared
#still dont understand the difference between shallow and deep copy in lists
print("shush")