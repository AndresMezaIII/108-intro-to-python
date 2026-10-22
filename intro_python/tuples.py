"""
tuples are immutable and created with parenthesis
"""

my_tuple = ("apple", "bannana", "cherry")

print(my_tuple) #tuples lock data that cannot be changed at all

#access items via indexing
print(my_tuple[2])

temp_tuple = ("apple", "bannana", "cherry")
temp_list = list(temp_tuple)
temp_list[0] = "Kiwi"
print(temp_list)
temp_tuple = tuple(temp_list)
print(temp_tuple) #the above lines incorporate the only means of updating a tuple, by copying the original tuple, casting it into a list, then editing it, and casting it back into a tuple

#single item tuple
new_tuple = ("water",) #tuple, note the comma
print(type(new_tuple))
not_tuple = ("apple") #the parenthesis are ignored and the value is read as a string, so always add the comma at the end even if it is a single value tuple
print(type(not_tuple)) #string

#joining, slicing, and looping
more_tuple = ("date", "elderberry")
print(my_tuple + more_tuple) #joins tuples into a new tuple
print(more_tuple * 2) #duplicates the tuple into one tuple
print(my_tuple[1:])

#loop through a tuple
for item in my_tuple:
    print(item)
#count and index
letters = ("a","b", "a", "c", "a")
print(letters.count("a")) #how many of a given value is in the tuple

print(letters.index("a")) #what index is value at (first appearance)

#tuple unpacking
#you can unpack a tuple's items directly into serparate variables
coords_tuple = (10, 20)
x, y = coords_tuple
print(x, y)

travel_bag = ("incinerator gun", "timbalands", "oversized bandaids", "black licorice chewing gum")
print(travel_bag[1], travel_bag[3])
if "shoes" in travel_bag:
    print("ready to walk")
else:
    print("No shoes. Bet you have your timbalands though.")

essentials = ("baby oil", "map of the old new york subway", "magic beans")
temp_list_two = list(travel_bag)
temp_list_three = list(essentials)
final_bag = tuple(temp_list_two + temp_list_three)
print(final_bag)

print(len(final_bag))
print(final_bag[-1])