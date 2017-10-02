from sys import argv

script, input_file = argv

def print_all(f):
	print f.read() #Prints everything and puts cursor at the end
	raw_input()	#Way of halting the program
def rewind(f):
	print f		#Wanted to see what it contains
	f.seek(0)	#Resetting the cursor to 0
	print f		#Could not figure out the difference between 2 prints
	raw_input()

def print_a_line(line_count, f):
	print f
	print line_count, f.readline(2)	#Reads linewise, argument takes number of bytes to read
	raw_input()

current_file = open(input_file)

print "First let's print the whole file: "
print_all(current_file)

print "Now let's rewind, kind of like a tape:"

rewind(current_file)	#Did not understand how the actual variable cursor is reset when formal variable is reset.

print "Let's print three lines:"

for i in range(5):
	print_a_line(i, current_file)
