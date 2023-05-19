# Write a program that receives a number and creates the following pattern. The number represents the largest
# count of stars on one row.
# *
# **
# ***
# **
# *

biggest_row = int(input())
for i in range(biggest_row + 1):
    print("*"*i)
for i in range(biggest_row - 1, 0, -1):
    print("*"*i)
