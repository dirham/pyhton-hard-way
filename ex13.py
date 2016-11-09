# Exercise 14: Prompting and Passing
from sys import argv

script, user_name = argv

promp = ">"

print "Hi, %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few question."
print "Do you like Me %s." % user_name
likes = raw_input(promp)

print "Where do you live %s" % user_name
lives = raw_input(promp)

print "What kind of computer you have %s" % user_name
computer = raw_input(promp)


print """
Alright, so you said %r about liking me.
you lives in %r. i don't know where is that.
And you have %r computer, nice.
""" % (likes, lives, computer)
