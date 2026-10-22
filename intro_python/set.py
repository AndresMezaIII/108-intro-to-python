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