# Exercise 16: Reading and Writing Files
from sys import argv
# we use ex14_sample.txt for file
script, filename = argv

print "We are going to earse this %r" %filename

print "If you won't that, press ctrl + c (^C)"

print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file...."
target = open(filename, 'w')

print "Truncate the file. Goodbay"
target.truncate()


print "Now i will ask you for three lines."

line1 = raw_input("line 1 :")
line2 = raw_input("Line 2 :")
line3 = raw_input("Line 3 :")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
# close and save that file

target.close()
