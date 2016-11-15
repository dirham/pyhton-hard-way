# Exercise 18: Names, Variables, Code, Functions

# *args sama seperti argv dapat menerima banyak parameter parbedaannya terletak penggunaannya
# jika argv digunakan untuk memasukkan parameter pada saat memanggil script python pada command line
# maka *argv digunakan untuk menampung variable pada fungsi ( parameter dalam fungsi disebut method )
def print_two(*args):
    print args
    arg1, arg2, arg3 = args
    print "arg1 : %r and arg2 : %r arg3 : %r" %(arg1, arg2, arg3)



# penggunaan *args pada saat ini tidak terlalu berguna kita dapat menggunakan cara lain seperti ini

def print_two_again(arg1, arg2):
    print "arg1 : %r, arg2 : %r" % (arg1, arg2)

def no_argumen():
    print "there is nothing argument"

# with *args you can put unlimited argument on function but if you use another var to
# catch value on *agrs you need to catch them all
print_two('put anything', 45, {3,5,6})

# this is only can take 2 argument and must be 2 argument
print_two_again("wan", "lan")
# this take no argument
no_argumen()
