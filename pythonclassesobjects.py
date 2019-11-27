"""
xteristics of an object
attributes
behavior

example
parrot is an object, attributes include ; name,age, color etc
behavior include; singing, dancing etc
Object- instantiation of class


Class- blue print for an object(sketch)
"""

class Person:

    #     # class attribute
    species = "Homo sapien"

    def __init__(self, name,age):
        print("I am the contractor method")
        self.jina = name
        self.miaka = age


    def walk(self):
        print("{}is walking".format(self.jina))
p12 = Person("Valentine", 26)
print(p12.jina)
print(p12.miaka)

# model a student
# school of that student abc primary school
# class 5
# marks for 5 subjects
#     score marks
#     create method to find total marks
#     method find the average
#     grade the student
    have a class/ contractor/methods total marks/averagescore/gradestudent




    #
#
#     # method -a functions defined inside a class
#     def walk(self):
#         print("{} is walking".format(self.name))
#
#     def sleep (alone):
#         print("is sleeping")


#
#
#
#
# p1 = Person()
# p1.name = "Valentine"
# p1.age = 26
# p1.height = 160
# p1.school = "techcamp"
# p1.citizenship ="kenyan"
# # print(p1.citizenship)
# # print(p1.school)
# # print(p1.height)
# # print(p1.name)
# # print(p1.age)
# # print(type(p1))
# # print(p1.species)
# p1.walk()
#
#
#
#
# # p2 = Person()
# # print(p2.species)
# # p3 = Person()
# # print(p3.species)
# # p4 = Person()
# # print(p4.species)
#
# # def__init__(self):- init method/constractor method
#
# class Car:
#     Model = "Toyota"
# car1 = Toyota()
# car1.wheel = "AloyReems"
# print(car1.wheel)
# car1.color = "WhineRed"
# print(car1.colo