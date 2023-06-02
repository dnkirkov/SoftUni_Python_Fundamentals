# Write a program that receives a sequence of numbers, separated by a single space, and prints their absolute value
# as a list. Use abs().

input_numbers = input().split()
abs_list = []
for num in input_numbers:
    abs_list.append(abs(float(num)))
print(abs_list)