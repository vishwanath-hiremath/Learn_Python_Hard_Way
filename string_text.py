x = 'There are %d types of people' %10 # New thing
binary = "Binary"
do_not = "don't"
y = "Those who know %s and those who %s"%(binary, do_not)

print x
print y

print "I said : %r" %x
print "I also said: '%s'" %y

hilarious = False
joke_eval = "Isn't that joke so funny! %r" # Interesting, can pass arguments while printing
# %r is used for debugging, as it prints the raw data
print joke_eval %hilarious

w = "This is left side of a..."
q = "a string with a right side"

print w + q
