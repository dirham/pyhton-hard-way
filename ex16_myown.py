# copying file with raw_input based on ex16

from os.path import exists

print "Test copying file, input name of file you want to copy below : "
copy_this = raw_input("")

# open and read the file input
read_copy = open(copy_this)
# must use var to assign read file
this_one = read_copy.read()

print "Now we ready to copy the file %r" % copy_this

to_file = raw_input("Enter the file name for new file : ")
print "file %r is exists ? %r" %(to_file, exists(to_file))
create_file = open(to_file,'w')
create_file.write(this_one)

print "Oke sir, all done !"
