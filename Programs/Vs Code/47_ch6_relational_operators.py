'''
Relational operators are used to evaluate conditions inside the if statements. Some examples of relational operators are :

== : equals
>= : greater than/equal to
<= : Less than/equal to
=! : Not equal to

'''

a = 18
b = int(input("Enter Your age : "))

if b==a:
    print("Your age is correct")
elif b>18:
    print("Your age is too high ")
elif b<18:
    print("You are not eligible")
else:
    print("Enter your correct age ")