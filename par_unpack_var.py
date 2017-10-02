#this program takes three arguments to run the program 
# Example: python par_unpack_var.py 1st 2nd 3rd
from sys import argv

script, first, second, third = argv
y = raw_input("Enter the fourth input here: ")
print "The script is called: ", script
print "Your first variable is: ", first
print "Your second variable is: ", second
print "Your third variable is: ", third
print "Your fourth variable is: ", y
