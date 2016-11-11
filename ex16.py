# Exercise 17: More Files

from sys import argv

from os.path import exists
script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# we could do this two line in one line, how ? using  semicolon
# like this : in_file = open(from_file);indata = in_file.read()
in_file = open(from_file)
indata = in_file.read()

print "the input file is %d bytes long" % len(indata)

print "Does the input file is exists ? %r" % exists(to_file)
print "Ready, hit enter to continue or ctrl + c to abort"
raw_input()
out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright all done"

out_file.close()
in_file.close()
