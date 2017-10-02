from sys import argv

script, filename = argv

print "We're going to erase %r." %filename
print "If you don't want that, hit CTRL+C now."
print "If you do want that, hit  RETURN now."

raw_input(">")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()	#Deletes the contents of the file

print "Now, I'm going to ask you for three lines."

line1 = raw_input("Line1: ")
line2 = raw_input("Line2: ")
line3 = raw_input("Line3: ")

print "I am going to write these to file."

target.write(line1 + "\n" + line2 + "\n" + line3)

print "And finally, We close it."
target.close()
