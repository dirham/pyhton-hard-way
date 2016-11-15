# use *args just like argv
def using_args(*args):
    print args

# using argument pass on Functions
def with_argument(arg1, arg2):
    print "arg1 : %r and arg2 : %r" % (arg1, arg2)

# using no argument and function will work perfectly without any errors
# but you can take or pass argument on this fucntion
def witt_no_arg():
    print 'nothing here'

# run or use fucntion

# just type the name of the fucntion to use them

# call using_args function
using_args("put anything", ['even', 'array'], 4)

# call with_argument
with_argument("this is arg 1", 8)

# call witt_no_arg
witt_no_arg()
