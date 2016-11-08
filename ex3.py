# the variable call car for total of cor
car = 100
# the variable to count space on the car
space_in_a_car = 4.0
# variable to put driver
driver = 30
# total of passengers
passengers = 90
# cars without driver
cars_not_driven = car - driver
# cars driven
car_driven = driver
# car pool
carpool_capacity = car_driven * space_in_a_car
# average passengers per car
average_passenger_per_car = passengers / car_driven

print "there are ", car, "cars available"
print "there are only ", driver, "Drivers available"
print "There will be ", cars_not_driven , "empty cars today"
print "We can transport ", carpool_capacity , "people today"
print "We have passengers", passengers ,"to carpool today"
print "We need to put about", average_passenger_per_car , "in each car"
