# You have a water tank with a capacity of 255 liters. On the first line, you will receive n – the number of lines,
# which will follow. On the following n lines, you will receive liters of water (integers),
# which you should pour into your tank.
# If the capacity is not enough, print "Insufficient capacity!" and continue reading the next line. On the last
# line, print the liters in the tank.

number_of_pours = int(input())
litres_in_tank = 0
for pours in range(number_of_pours):
    pour = int(input())
    if litres_in_tank + pour > 255:
        print("Insufficient capacity!")
    else:
        litres_in_tank += pour
print(litres_in_tank)
