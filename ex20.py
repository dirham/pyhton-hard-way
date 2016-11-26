def add(a,b):
    print "Adding %d + %d" % (a, b)
    return a + b

def subtract(a,b):
    print "SUBTRACTING %d = %d"% (a,b)
    return a - b

def multiply(a,b):
    print "Multiply %d * %d"% (a, b)
    return a * b

def devided(a, b):
    print "Devided %d / %d"% (a,b)
    return a/b


print "Let's do some math with just Functions"

age = add(4,5)
height = subtract(74, 2)
weight = multiply(90, 2)
iq     = devided(100, 2)

print "Age : %d, height : %d weight : %d, and Iq : %d" % (age, height, weight, iq)
# A puzzle for the extra credit
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, devided(iq,2))))

print "That's becomes: ", what, "can you do that by the hand?"
