'''
Tuples in python
    A tuple is an immutable (unchangeable) data type in python

    a = () --> Empty tuple
    a = (1,) --> Tuple with only one element needs a comma
    a = (1, 7, 2) --> Tuple with more than one element
    
    Once defined a tuples elements cant be altered or manipulated.
'''


# Creating a tuple using ()
t = (1, 2, 4, 5)
t1 = () # Empty tuple 
t1 = (1) # Wrong way to declare a tuple with single element 
t1 = (1,) # tuple with single element 
print(t1)

# Printing the elements of a tuple
# print(t[0])

# Cannot update the value of a tuple
# t[0] = 34 # throws an error
