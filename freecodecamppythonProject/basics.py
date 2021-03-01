"""to use all the different math functions that python has you will need to import them by using the statement below"""

from math import *

print("Hello World")

"""basic triangle"""
print("    /|")
print("   / |")
print("  /  |")
print(" /_ _|")

"""This is how i do a new line in python can also use \" to do the same"""
print("Patience\n Ndlovu")

""" Functions"""
phrase = "Python is cool"

"""changes the variable to lowercase"""
print(phrase.lower())

"""changes the variable to uppercase and checks that its in uppercase"""
print(phrase.upper().isupper())

"""will tell you how many characters in the phrase"""
print(len(phrase))

"""used to find out what character is at the said index position"""
print(phrase[4])

"""This is called passing a parameter and it will give you the index number"""
print(phrase.index("c"))

"""replace function is used to change the statement"""
print(phrase.replace("Python", "Coding"))

"""Numbers basics - see statement at the top about imports"""

print(2 * (3 + 5))

print(10 % 3)

my_number = 5
print(my_number)
print(str(my_number) + " my favourite number ")

"""abs is absolute values """
print(abs(my_number))

"""pow is the power of"""
print(pow(3, 2))

print(round(5.1278))

print(sqrt(100))

"""Inputs examples """
name = input("Enter your name: ")
last_name = input("Enter your last name: ")
print("Hello " + name + " " + last_name + "!")


