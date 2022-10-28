'''
input() function
This function allows the user to take input from the keyboard as a String
'''
a = input("Enter a number: ")     #  => If a is "gaurav", the user entered gaurav
a = int(a)  # Convert a to an integer (if possible)
print(type(a))

'''
It is important to note that
the output of input is always      =>      If a is "34" user entered 34
a String (even if the number
is entered)
'''