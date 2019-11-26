
# FUNCTIONS
# A group of related python statement that perform
# Keyword def marks the start of function header./ a_name/()/:/#body/- marks the function header
# parameters- a variable that is used inside a function
# A function name to uniquely identify it. for example from above our function name is called "function". Nb:Follow rules of naming variables.
# Parameters (arguments) through which we pass values to a function. NB: This is option.
# A colon (:) to mark the end of function header.
# Optional documentation string (docstring) to describe what the function does.
# One or more valid python statements that make up the function body.  NOTE: make your function body is indented(usually 4 spaces)
# An optional return statement to return a value from the function.

# def add_two_numbers(a,b)
#     sum= a+b
#     return sum
# ans=add_two_numbers(30,10)
# print(ans)

# You've got chickens (2 legs), cows (4 legs) and pigs (4 legs) on your farm. Return the total number of legs on your farm. (CREATE A FUNCTION)
#
# example:
#
# animals(2, 3, 5) ➞ 36
#
# animals(1, 2, 3) ➞ 22
#
# animals(5, 2, 8) ➞ 50

# def number_of_legs (chickens,cows,pigs):
#     sum = (2*chickens)+(4*cows)+(4*pigs)
#     return(sum)
# legs1= number_of_legs(2,3,5)
# legs2= number_of_legs(1,2,3)
# legs3= number_of_legs(5,2,8)
# print(legs1)
# print(legs2)
# print(legs3)



# Create a function that takes a list of numbers. Return the largest number in the list.
# example
# findLargestNum([4, 5, 1, 3]) ➞ 5
# findLargestNum([300, 200, 600, 150]) ➞ 600
# findLargestNum([1000, 1001, 857, 1]) ➞ 1001

# def list_of_numbers (alist):
#     maximum = max(alist)
#     return maximum
# print(list_of_numbers([4,5,1,3]))
# print(list_of_numbers([300,200,600,150]))
# print(list_of_numbers([1000,1001,857,1]))





# Given a list of integers, return the difference between the largest and smallest integers in the list.
# example:
# difference([10, 15, 20, 2, 10, 6]) ➞ 18
# # 20 - 2 = 18
# difference([-3, 4, -9, -1, -2, 15]) ➞ 24
# # 15 - (-9) = 24

# def diff_integers(alist):
#     diff = max(alist)-min(alist)
#     return diff
# print(diff_integers([10,15,20,2,10,6]))
# print(diff_integers([-3,4,-9,-1,-2,15]))

"""
Create a function to concatenate two integer lists.

example:

concat([1, 3, 5], [2, 6, 8]) ➞ [1, 3, 5, 2, 6, 8]

concat([7, 8], [10, 9, 1, 1, 2]) ➞ [7, 8, 10, 9, 1, 1, 2]

concat([4, 5, 1], [3, 3, 3, 3, 3]) ➞ [4, 5, 1, 3, 3, 3, 3, 3]


"""

def concat_ints(list1,list2):
    combine = list1 + list2
    return combine
print(concat_ints([1,3,5],[2,6,8]))
print(concat_ints([7,8],[10,9,1,1,2]))
print(concat_ints([4,5,1],[3,3,3,3,3]))


"""

Create a function that takes two strings as arguments and return either True or False depending on whether the total number of characters in the first string is equal to the total number of characters in the second string.

example:

comp("AB", "CD") ➞ True

comp("ABC", "DE") ➞ False

comp("hello", "edabit") ➞ Fals
b
"""
def comp (string1,string2)
    lenstringA= len(string1)
    lenstringB= len(string2)
    if lenstringA == lenstringB:
        return True
    else:
        return False

#OR
def comp (string1,string2)
    if if len == lenstringB:

# practice question
# We should create a function that ‘findsgrade’ by
# taking in marks of each subject as parameters
# calculating total from the parameters(subjects) passed
# calculating the average from the total
# using if statement to find grade
# what if I want to get total marks! and average?