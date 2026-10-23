animals = ["catfish", "komodo dragon", "giraffe", "red panda", "blue whale"]

print(animals)

print(f"My favorite animal is the {animals[2]}") #access the animal at index two, komodo dragon

print(animals)

animals[1] = "alligator garr" #change the object and index 1, item 2, with "alligator garr"

print(animals)

animals.pop() #remove the last object in the list

print(animals, len(animals))

#create a dictionary
my_dictionary = {
    "user": "donnie brasco",
    "platform": "snapchat",
    "is_active": False
}

#access the value of the key user
print(my_dictionary["user"])

#adding a dictionary item
my_dictionary.update({"years of service": 10})

print(my_dictionary)

my_dictionary.pop("platform")

print(my_dictionary, len(my_dictionary))


