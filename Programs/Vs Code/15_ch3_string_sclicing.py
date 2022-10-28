'''
String sclicing
    A string in apython can be scliced for getting a 
    part of the string.
    consider the following string :

    name = "G    a    u    r    a    v" =>  length = 5
            0    1    2    3    4    5
          (-6) (-5) (-4) (-3) (-2) (-1)

The index in a string starts from 0 to (length-1) in 
python. In order to sclice a string, we use the 
following syntax : 

    sl = name [ind_start : ind_end]
    ind_start --> first index included
    ind_end --> cast index index is not included        

    sl [0:3] returns "Gau"  --> Character from 0 to 3
    sl [1:3] returns "au"   --> Characters from 1 to 3
'''


# greeting = "Good Morning "
# name = "Gaurav"
# print(type(name))

# Concatenating two strings
# c = greeting + name
# print(c)

name = "Gaurav"
# ṇprint(name[0])
# name[3] = "d"  --> Does not work

# print(name[0:3])
# print(name[:4]) # is same as name[0:4]
# print(name[1:]) # is same as name[1:6]
# c = name[-5:-1] # is same as name[1:4]
# print(c)

'''
Slicing with skip value
    -- We can provide a skip value as a part of our slice like this : 

        word = "amazing"
        word[1:6:2] --> 'mzn'

Other Advance slicing techniques
        word = "amazing"
        word [:7] --> word [0:7] --> 'amazing'
        word [0:] --> word [0:7] --> 'amazing' 
'''

name = "GauravIsGood"
d = name[0::3]
print(d)
