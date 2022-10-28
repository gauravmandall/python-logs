# Creating an empty set
b = set()
print(type(b))

# Adding values to an empty set
b.add(4)
b.add(5)
b.add(5)
b.add(5) # Adding a value repeadly does not changes a set
b.add((4, 5, 6))

# # Accesing Elements
# b.add({4:5}) # Cannot add list or dictionary to sets
print(b)

# Length of the set
print(len(b)) # Prints the length of this set

# Removal of an Item
b.remove(5) # Remove 5 from set b
# b.remove(15) # Throws an error while trying to remove 15 (which is not present in the set)
print(b)

print(b.pop())
print(b)
