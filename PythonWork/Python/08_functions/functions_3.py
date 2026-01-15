def greet():
     print("Hello, World!")

greet()
greet()
greet()
greet()
print("SHSUH")
greet()    


def collect_student_details():
     name = input("Enter your name: ")
     age = input("Enter your age: ")
     mobile = input("Enter your mobile: ")
     first_name = name.split()[0]
     last_name = name.split()[0]
     print("First Name:", first_name)
     print("Last Name:", last_name)
     print("Age:", age)

collect_student_details()
def display_details():
     print("name :", name )
     print(f"age: { age }")



def display_details(name, age,  email , mobile):
    print("name :", name )
    print(f"age: { age }")
    print("email :", email )
    print("mobile :", mobile )

display_details("John Doe", 20, " jdoe.gmail.com", "123-456-7890")
display_details("Jane Smith", 22, "jsmith.gmail.com", "098-765-4321")

#if only one parameter is passed
# display_details("Alice", 19)
#will show error because email and mobile are missing
#TypeError: display_details() missing 2 required positional arguments: 'email' and 'mobile'
def display_details(name, age, email="Not Provided", mobile="Not Provided"):
    print("name :", name )
    print(f"age: {age}")
    print("email :", email )
    print("mobile :", mobile )
display_details("Alice", 19)
#will work fine now as email and mobile have default valuesw
print("shush")
