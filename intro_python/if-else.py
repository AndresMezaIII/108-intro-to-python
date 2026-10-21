"""
a conditional control structure allowing developers 
to specify a codeblock based on whether a condition 
is true or false
"""

#if condition:
    #code to run
#elif another condition: 
    # code to run if 1st statement is false but the new 
    # condition is true
    #any number of elifs can be specified
#else:
    #code runs if all other conditions are false, not necessarily 
    #because a statement is true or false, it is not checked against 
    #a statement

x = 10

if x > 0:
    print("x is positive")
elif x == 0:
    print("x is zero")
else:
    print("x is negative")

#below is a one line structure for simple if conditions
if x > 5: print("x is greater than 5")

#shorthand if/else
print("even") if x % 2 == 0 else print("odd")

#nested if, both ifs must be true
if x > 0:
    if x < 20:
        print("x is a positive number less than 20")

#combining conditions
age = 20
if age >= 18 and age <= 20:
    print("You are between 18 and 21")