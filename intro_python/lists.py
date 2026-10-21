"""
lists are ordered, changeable, index based sequences that can contain duplicate items. They are used to store multiple data types in a single variable. They are created using [ ]
"""

my_list = [1,2,3,4,5]
print(my_list)

#mixed list
mixed_list = [1, "Hello", True, 22.4]
print(mixed_list)

#accessing items by index
print(mixed_list[0], my_list[4])

#you can use negative indexing to count in reverse
print(mixed_list[-2], my_list[-3])

#slicing lets you specify a range of items [start:stop:step]
numbers = [0,1,2,3,4,5,6,7,8,9]
print(numbers[3:6]) #index 3-6 (index positions)
print(numbers[:8]) #index 0-7 (index positions)
print(numbers[::2]) #index the whole list by two's

#update the numbers list
numbers[3] = 26
print(numbers)

numbers.append(99) #add 99 to the end of the list
numbers.pop(4) #remove the item at index 4, no index removes the last item
numbers.insert(1, "yeah") #insert "yeah" at index 1
numbers.extend([3,6,9]) #add multiple to the end of the list
print(numbers)
numbers.remove(99) #remove the first occurrence of value
print(numbers)

#numbers.clear() #removes all items in the list
#print(numbers)

#looping through a list
for number in numbers:
    print(number)

print(len(numbers))

#useful list methods
new_numbers = [4,2,6,1,8,8,0]
print(new_numbers.count(8)) #return the number of occurrences of value

print(new_numbers.index(4)) #return the index of the first occurrence of value

new_numbers.sort() #sort list from smallest to largest or alphabetical order
print(new_numbers)

new_numbers.sort(reverse=True) #sort the list and print it from the last value to the first
print(new_numbers)

groceries = ["apples", "cereal", "sprite", "bread", "coffee"]
print(groceries[0],groceries[-1])
print(groceries[:3])
groceries.append("eggs")
print(groceries)
groceries.insert(0,"milk")
print(groceries)
groceries.remove("sprite")
print(groceries)
if "bread" in groceries:
    print("Bread is in the list")
elif "bread" not in groceries:
    print("No bread")
else:
    print("...")
groceries.sort()
print(groceries)
