# Calculate how many courses will be needed to elevate N persons by using an elevator with a capacity of P persons.
# The input holds two lines: the number of people N and the capacity P of the elevator.

import math

people = int(input())
elevator_capacity = int(input())
number_of_courses = math.ceil(people / elevator_capacity)
print(number_of_courses)

