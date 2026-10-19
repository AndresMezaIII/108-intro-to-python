print("Hello world!")
print(2)
print(5+3)
print(True)
#single line comment
"""
multi-line 
        comment


"""
# varName = value
name = "Andres"
age = 44
print(name, age)

#Concatenation
# below, str() cast the variable age as a string type to concatenatet the values in the 
# print statement
print("Hello my name is " + name + " and I am " + str(age))

name = "Romeo"
age = 86
scary = True
favorite = 647
fname = "Juliette"

#concatenation is an old method for printing
print(name + " is " + str(age) + " years old. His favorite person, " + fname + ", is " + str(favorite) + " and she is scary, " + str(scary) + ".")
#FSTRING
print(f"{name} is {age} years old. His favorite person, {fname} is {favorite} and, she is scary, {scary}.")
#MULTILINE FSTRING
print(f"""testing
                        testing
        testing
""")

#type() function
print(type(name))
print(type(age))
print(type(scary))

#input function always returns a string: input()
user_name = input("What is your name?: ")
print(f"Hello, {user_name}!")
#print input as a string
new_age = int(input("Enter your age: "))
print(type(new_age), new_age)
print(new_age + new_age)

pizzas = int(input("How many pizzas do you have?: "))
people = int(input("How many people are eating pizza?: "))
print(f"There are enough pizzas for {(pizzas * 8) // people} slices per person!")

x = 1
y = 2
z = 2
res = x + y
print(res)
res = x - y
print(res)
res = x * y
print(res)
res = x / y
print(res)
res = x // y
print(res)
res = z % y
print(res)
res = x ** y

# +=, -=, *=, and /= are all shortcuts for math operation assignment
# <= >= < > != ==
# and, or, not

x = 2
y = 10
z = 10

print(x == y and y == z) 
print(x == y or y == z)
print(x != y)
print(y != z)

#Identity operator
# - is check if two items are the exact same object in memory
# - not checks if they are NOT the same object in memory

x = 3
y = 3

print(x is y)
print(x is not y)

#membership operator - used to test if a sequence is present in an object (in or not in an array or object)

x = [1,2,3,4,5]

print(5 in x)
print(9 not in x)