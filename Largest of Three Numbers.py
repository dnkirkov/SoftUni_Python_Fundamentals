# Write a program that receives three whole numbers and prints the largest one.

largest_number = int(input())
for i in range(2):
    current_number = int(input())
    if current_number > largest_number:
        largest_number = current_number
print(largest_number)
