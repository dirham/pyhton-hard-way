# Exercise 19: Functions and Variables

from sys import argv
script, nameFu = argv
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"


print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)


print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)


print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)


# my own Functions
def myown(arg):
    print "my arg : %r" %arg


# call myown function
# 1
myown("test 1")
# call function to variables
test2 = myown("from var")
test2
# call using argv is not work
nameFu
print "%r" %nameFu

# using user input to call function
# also didn't work
test3 = raw_input("enter func name : " )
test3(7)
