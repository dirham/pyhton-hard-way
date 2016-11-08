my_name = "Dirham"
my_age  = 23 #this is my real ages
my_height = 160 # cetimeter
my_weight = 55 #kg
my_eyes   = "blue"
my_teeth  = "White"
My_hair   = 'Black'
height_to_inch = my_height / 2.5
beck_to_cm = height_to_inch * 2.5
print "This my Height %d if I using inch beside a cm" % height_to_inch
print "And if I used cm inside inch my Height is %d" % round(beck_to_cm)
print "what is round function do %r" % round(1.77)
print "Now i Know what round function do "
print "Let's talk about %s." % my_name
print "He is %d centimeter tall" % my_height
print "He's %d kg heavy " % my_weight
print "Actually, that's not to heavy"
print "He's got %s eyes and %s Hairs." % (my_eyes, My_hair)
print "His teeth are usually %s depending on the coffee :)" % my_teeth

#this line try using arithics inside printing format
print "If I add %d, %d, and %d I get %d." % (my_age,my_height, my_weight, my_age + my_height + my_weight)
