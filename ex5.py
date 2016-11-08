# just like excercise beforem=, but now put string format into variable
x      = "There are %d types of people." % 10
binary = "Binary"
d_not  = "don't"
y      = "Those who knows %s and those who %s" % (binary, d_not)


print x
print y

# %r is very usefull for debugging for know what inside the variable
print "I said : %r" % x
print "I also said : '%s'." % y

# assign boolean value into hiralious var
hiralious = False
joke_evaluation = "Isn't that joke so funny ?! %r"
# print joke_evaluation with whatever format in a hiralious var (%r)
print joke_evaluation % hiralious
# prepare string into var for print
w = "This is the left side of..."
e = "a string with a right side."

print w + e # adding two string just like number
