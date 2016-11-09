# read and write file using python

from sys import argv

script, file_to_open = argv

print "Hy, you want to open this %r, file ?" % file_to_open

print "If so then please press enter or if not press ctrl + c"

raw_input("your answer ?")

print "So you want to open and write this %r file" % file_to_open
print "We don't use truncate anymore becouse using open(file, 'w'), will overwrite the file so truncate is not necessary"

print "Trying to open and write file...."
files = open(file_to_open,'w')

print "let's write on the file %r" % file_to_open

fline = raw_input("Write the first line :")
sline = raw_input("Write the second line : ")
tline = raw_input("Write the next line : ")

files.write("%s\n%s\n%s\n"% (fline, sline, tline))

print "Let's close and save that file"

files.close()
