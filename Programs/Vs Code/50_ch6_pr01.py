# Write a program to find greatest of four numbers entered by the user.


a = int(input('Enter your First number : '))
b = int(input('Enter your Second number : '))
c = int(input('Enter your Third number : '))
d = int(input('Enter your Forth number : '))


# Method 1

# if(a>b and a>c and a>d):
#     print("The greatest number is ", a)
# elif(b>c and b>d and b>a):
#     print("The greatest number is ", b)
# elif(c>d and c>a and c>b):
#     print("The greatest number is ", c)
# else:
#     print("The greatest number is ", d)



# Method 2 

if(a>b): 
    f1 = a          # here we compare a and b 
else:               # Which number is greater that will store in f1
    f1 = b

if(c>d):
    f2 = c          # here we compare c and d
else:               # Which number is greater that will store in f2
    f2 = d

if(f1>f2):
    print(str(f1) + " is greater.")     # here we compare f1 and f2 
else:                                   # which one is greater that will print.
    print(str(f2) + " is greater.")