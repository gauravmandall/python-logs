''' Dictionary & Sets
Dictonary is a collection of key - Value pairs

Syntax :
    a = {"key"      :   "Value",
         "gaurav"   :   "Code",
         "marks"    :   "100",
         "list"     :   [1, 2, 9]}

a["key"] => Prints "value"
a["list "] => Prints [1, 2, 9]
'''
# Properties of a Python Dictionaries
'''
1> It is unordered
2> It is mutable 
3> It is indexed
4> Cannot contain duplicate keys
'''

myDict = {
    "Fast": "In a Quick Manner",
    "Gaurav": "A Coder",
    "Marks": [1, 2, 5],
    "anotherdict": {'gaurav': 'Player'}
}

print(myDict['Fast'])
print(myDict['Gaurav'])
print(myDict['Marks'])
print(myDict['anotherdict']['gaurav'])

