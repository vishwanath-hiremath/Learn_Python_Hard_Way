# This one is like script with argv
def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r arg2: %r" %(arg1, arg2)

#Similar to previous one without pointers
def print_two_again(arg1, arg2):
	print "arg1: %r arg2: %r" %(arg1, arg2)

#Function with one argument
def print_one(arg1):
        print "arg1: %r" %(arg1)

#No argument
def print_none():
	print "No argument"

print_two("Vishwanath", "Hiremath")
print_two_again("Smriti", "Gupta")
print_one("Geetika")
print_none()
