# Write a program that rounds all the given numbers, separated by a single space, and prints the result as a list. Use
# round().

numbers = input().split()
round_list = []
for num in numbers:
    round_list.append(round(float(num)))
print(round_list)
