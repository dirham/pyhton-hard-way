# modify excercise ex16.py with raw_input

# import package

from os.path import exists

print "oke let's enter the file you want to open"
file_to_open = raw_input("enter the file name : ") # oke.xt or what you want 

read_file = open(file_to_open)
cp_read = read_file.read()

cp_name = raw_input("Oke now enter the name you want for duplicate name : ")
print "check file name exists or not ? %r" % exists(cp_name)

cp_this = open(cp_name,'w')
cp_this.write(cp_read)

print "Finising up"

cp_this.close()
read_file.close()
print "All done sir"
