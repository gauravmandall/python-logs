'''
Create an empty dictionary. Allow 4 friends to 
enter their favorite language as values and use 
keys as their names.Assume that the names are unique
'''
favLang = {}
a = input("Enter your favorite language Shivam : ")
b = input("Enter your favorite language Kunal  : ")
c = input("Enter your favorite language Manish : ")
d = input("Enter your favorite language Gaurav : ")
favLang['Shivam'] = a
favLang['Kunal '] = b
favLang['Manish'] = c
favLang['Gaurav'] = d

print(favLang)


# Answer of practice set 07 :
# When two names are same the output will be updated as per latest input.

# Answer of parctice set 08 :
# when two or more keys are same the program will run normally.