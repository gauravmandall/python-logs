myDict = {
    "fast" : "In Quick Manner",
    "gaurav" : "a Coder",
    "marks" : [1, 2, 5],
    "anotherDict" : {'gaurav' : 'Player'},
    1 : 2
}

# Dictionary Methods
print(list(myDict.keys())) # Prints the keys of the dictionary
print(myDict.values()) # Prints the keys of the dictionary
print(myDict.items()) # Prints the (key, values) for all contents of the dictionary
print(myDict)
updateDict = {
    "shivam" : "Friend",
    "divya" : "Friend",
    "kunal" : "Friend",
    "gaurav" : "A Hacker"
}
myDict.update(updateDict) # Updates the dictionary by adding key-value pairs from updateDict
print(myDict)

print(myDict.get("gaurav")) # Prints value associated with key "gaurav"
print(myDict["gaurav"])  # Prints value associated with key "gaurav"

# The difference between .get and [] syntax in Dictionaries?
print(myDict.get("gaurav2")) # Returns none as gaurav2 is not present in the dictionary 
print(myDict["gaurav2"])  # Throws an error as gaurav2 is not present in the dictionary

# Hint --> More Methods available in docs:python.org