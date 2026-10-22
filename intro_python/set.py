"""
sets are unordered, unchangeable, collections that don't allow duplicates. because they are unordered they are unindexed. create them with {}
"""
#every time a new print function is called the order of the items in the set will change
fruits = {"apples", "bannana","cherry"}
print(fruits)

#prints will remove duplicates
fruits = {"apples", "bannana", "apples"}
print(fruits)

#removing duplicates from sets
emails = ["@yahoo.com", "@hotmail.com", "@hotmail.com", "@hotmail.com", "@outlook.com", "@gmail.com", "@hotmail.com"]

unique_emails = set(emails)

print(emails, unique_emails)
print(list(unique_emails))

fruits.add("oranges") #add one item to the set

#add multiple items to the set
fruits.update(["pears", "kiwi", "mango"])
print(fruits)

#remove items from a set if it exists if it doesn't, raises a key error
fruits.remove("bannana")

#if an item doesn't exist and you use discard it will silently ignore otherwise it will discard the value if present.
fruits.discard("oranges")
print(fruits)

#set operations always results in an ordered set
set_one = {1,2,3,4}
set_two = {3,4,5,6}

print(set_one.union(set_two)) 
#returns a union of two sets, with no duplicates, as a new set

print(set_one.intersection(set_two)) #returns the values which are common to both sets

#returns the values of the specified set that are different or unique from the compared to set
print(set_one.difference(set_two))

#symmetric difference
print(set_one.symmetric_difference(set_two)) #return everything except what is shared (unique elements of both sets)

group_a = {"leo", "sam", "alex", "nina"}
group_b = {"nina", "jordan", "sam", "taylor"}

print(group_a.intersection(group_b))
print(group_b.symmetric_difference(group_a))

signin = ["leo", "nina", "leo", "maya", "nina", "sam"]
print(set(signin))

group_list = list(group_a) + list(group_b)
group_registered = group_a.union(group_b)
unregistered = set(group_list).symmetric_difference(set(signin))

#FOR LOOPS
for letter in "Hello":
    print(letter)

#range prints the index number of a range, not the value
for x in range(5):
    print(x)

for x in range(2, 6): #start at 2 and print to index 6
    print(x)

#step skips number
for x in range(0, 10, 2):
    print(x)    #start at 0, end at 10, count by 2's


#else in for loops
for x in range(3):
    print(x)
else: #in a for loop, else is the next step, not conditional execution
    print("loop done")

#else is most useful with break
for number in [3,7,9]:
    if number % 2 == 0:
        print("Found an even number")
        break #stops the loop
else:
    print("No even numbers found")

#break and continue in for loops
for x in range(10):
    if x == 5:
        continue
    if x == 8:
        break
    print(x)

num = input("Enter a number: ")
for x in range(1,11):
    i = int(num) * x
    print(f"{i} x {x} = {i * x}")

#While loops run as long as a condition is true. If it never becomes false, you can get an infinite loop

count = 1
while count <= 5:
    print("Count is ",count)
    count += 1 #add to count so that the condition can become false

count = 0
while count < 5:
    count += 1
    if count == 3:
        continue #skips three and continues after it with no logic execution
    print(count)
else:
    print("Loop finished")

tasks = ["dishes", "garbage", "homework"]
while tasks:
    current = tasks.pop()
    print("Doing", current)

while True:
    answer = input("Enter a number: ")
    try:
        number = int(answer)
        break
    except ValueError:
        print("That's not a number")

print(f"Thanks! You entered {number}")