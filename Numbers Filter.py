# On the first line, you will receive a single number n. On the following n lines, you will receive integers.
# After that, you will be given one of the following commands:
# • even
# • odd
# • negative
# • positive
# Filter all the numbers that fit in the category (0 counts as a positive and even). Finally, print the result.

count = int(input())
number_list = []
filtered_list = []
for i in range(count):
    number = int(input())
    number_list.append(number)
command = input()
if command == 'even':
    for num in number_list:
        if num % 2 == 0:
            filtered_list.append(num)
elif command == 'odd':
    for num in number_list:
        if num % 2 != 0:
            filtered_list.append(num)
elif command == 'positive':
    for num in number_list:
        if num >= 0:
            filtered_list.append(num)
elif command == 'negative':
    for num in number_list:
        if num < 0:
            filtered_list.append(num)
print(filtered_list)
