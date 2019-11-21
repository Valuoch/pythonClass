# if...else statements in python
# syntax:

# if test_expression:
#     //statements

# number = 100


# a) if
# if number > 50:
#     print("I am ok.")

# b)if...else
# if number > 150:
#     print("I am ok.")
# else:
#     print("I am not ok.")

#c)if...elif

# num = 20
#
# if num > 0:
#     print(" {} is > 0".format(num))
#
# elif num == 10:
#     print(" {} is == 0".format(num))
#
# else:
#     print(" {} is a negative number".format(num))

# num = -100
num = int(input("Enter a number:"))
if num > 0:
    print(" {} is > 0".format(num))

elif num == 10:
    print(" {} is == 0".format(num))

else:
    print(" {} is a negative number".format(num))


# Assigment:
#1. Create a program to ask student name and ask for marks of 5 subjects eg kiswahili, english etc
#     a)find total marks
#     b)find the average makes
#     c)grade the student
#2.assume u have makes for 10 students and rank them