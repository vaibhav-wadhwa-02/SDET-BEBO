
# 1 Ans
"""
a = 15
b = 1.0
c = "vaibhav"
d = True

print(f"value in variable a is {a}  and datatype is ",type(a))
print(f"value in variable b is {b}  and datatype is ",type(b))
print(f"value in variable c is {c}  and datatype is ",type(c))
print(f"value in variable d is {d}  and datatype is ",type(d))
"""


# 2 Ans
'''
var = 12
print(var)
del var
print(var)
'''

# 3 Ans
'''
print(help("keywords"))
help("keywords")
'''

# 4 Ans
'''
var1 = 9
var2 = 3
print(f"Addition of the {var1} and {var2} is : ", var1+var2 )
print(f"Subtraction of the {var1} and {var2} is : ", var1-var2 )
print(f"Multiplication of the {var1} and {var2} is : ", var1*var2 )
print(f"Division of the {var1} and {var2} is : ", var1/var2 )
print(f"Modulus of the {var1} and {var2} is : ", var1%var2 )
print(f"Exponentiation of the {var1} and {var2} is : ", var1**var2 )
print(f"Floor division of the {var1} and {var2} is : ", var1//var2 )
'''

# 5 Ans
'''
str1 = "Bebo"
str2 = "Technologies"
print(f"concadination of var = {str1} and  var = {str2} is : ", str1+str2)
'''

# 6 Ans
'''
name = "Vaibhav"
print("1 My name is ", name)
print(f"2 My name is {name}")
print("3 My name is {} ".format(name))
'''

# 7 Ans
'''
colour = input("Enter your favourite colour : ")
print(f"Favourite colour of user is {colour}")
'''

# 8 Ans
'''
var1 = int(input("Enter the number of your choice : "))
var2 = float(input("Enter the number of your choice : "))
print(f"The number enetred by the user is {var1}  and its type is ", type(var1))
print(f"The number enetred by the user is {var2}  and its type is ", type(var2))
'''

'''
# 9 Ans
firstname = input("Enter First name : ")
lastname = input("Enter Last name : ")
age = int(input("Enter your age : "))
# firstlast = firstname+" "+lastname
print(f"Hello {firstname+" "+lastname} you are {age} years old")
'''

'''
# 10 Ans
a = 10
b = 20
print(a is b)
print(a is not b)
'''

'''
# 11 Ans
a = 2
b = 3
print(a & b)
print(a | b)
print(a ^ b)
print(a ~ b)
print(a << b)
print(a >> b)
'''

# 12 Ans
'''
# grade A above 89
# grade B above 79
# grade C above 69
# grade D above 59
# grade F below 60

marks = int(input("Enter the number you scored : "))
if marks>89:
    print("Your Grade is A ")
elif marks>79:
    print("Your Grade is B ")
elif marks>69:
    print("Your Grade is C ")
elif marks>59:
    print("Your Grade is D ")
else:
    print("Your Grade is F ")
'''

# 13 Ans
'''
age = int(input("Enter your age : "))
if age>=18:
    print("Congratulations! Your are elibible to vote. ")
else:
    print("OOPS! You are not elibile to vote this time. ")
'''

# 14  Ans
'''
num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the Second number : "))
num3 = int(input("Enter the Third number : "))

print("your entered numbers are : ", num1,num2,num3)
# 10 20 30
if num1 is num2 or num1 is num3 and num2 is num3:
    print("some numbers are equal")
    exit
else:
    if num1>num2 and num1>num3:
            print("num 1 is greater ")
    elif num2>num1 and num2>num3:
            print("num 2 is greater")
    elif num3>num1 and num3>num2:
            print("num 3 is greater")
'''

# 15 Ans
'''
inp = int(input("Enter any number between 0 - 99 "))
if inp > 99:
    print("Perhaps! your number is more than 99")
else:
    print(f"Congo! your number {inp} Falls in the range")
'''

# 16 Ans
'''
str1 = "Bebo"
str2 = "tech"
print(str1==str2)
'''

# 17 Ans
'''
hindi = 79
english = 87
maths = 92
science = 91
average = hindi+english+maths+science/4

if maths>80 and science>70:
    print(f"Congo! You are elibile for the course")
elif average>75:
    print(f"Congo! you are Elibile for the course")
else:
    print("Oops, You are not Elibile this time")
'''

# 18 Ans
'''
username = "Vaibhav"
password = "Vaibhav@123"
userInp = input("Enter username : ")
passInp = input("Enter password : ")

if userInp == username and password == passInp:
    print("Logged In")
elif userInp != username or password != passInp:
    print("username password doesn't matched")
'''

# 19 Ans
'''
age = int(input("Enter your age : "))
if age>=18:
    print("Congratulations! Your are elibible to drive. ")
else:
    print("OOPS! You are not elibile to drive. ")
'''

# 20 Ans
'''
num1 = -10
num2 = 21
if num1 > 0 and num2 > 0:
    print("Any number is positive")
elif num1<0 and num2<0:
    print("Any number is negavtive")
else:
    print("numbers having mixed signs")
'''

# 21 Ans
'''
day = input("Enter the day : ")
match day:
    case "sunday":
        print("It's the weekend!")

    case "saturday":
        print("It's the weekend!")

    case "monday":
        print("It's a weekday")

    case "tuesday":
        print("It's a weekday")

    case "wednesday":
        print("It's a weekday")

    case "thursday":
        print("It's a weekday")

    case "friday":
        print("It's a weekday")
break statement or not operator instead ! or ==


# Swapping of a number
num1 = 12
num2 = 23
# Method 1
num1,num2 = num2,num1
# Method 2  using third variable
temp = num1
num1 = num2
num2 = temp
# Method 3 without using third variable
num1 = num1 - num2
num2 = num2 - num1
num1 = num1 + num2

'''
# even or odd
'''
if num1%2==0:
    print("the number is a even number")
else:
    print("The number is a odd number")
'''
