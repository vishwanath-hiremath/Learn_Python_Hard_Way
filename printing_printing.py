formatter = "%r %r %r %r" # Can take four arguments of any datatype 

print formatter %(1, 2, 3, 4)
print formatter %("one", "Two", "Three", "Four")
print formatter %(True, False, True, False)
print formatter %(formatter, formatter, formatter, formatter) #Interesting
print formatter %('I had this thing \n', "That you could type right \n", "But it didn't sing \t", "So I said goodnight :-)")
