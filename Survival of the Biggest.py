# Write a program that receives a list of integer numbers (separated by a single space) and a number n. The number n
# represents the count of numbers to remove from the list. You should remove the smallest ones, and then, you
# should print all the numbers that are left in the list, separated by a comma and a space ", ".

my_list = input().split()
numbers_remaining = int(input())
int_list = []
for index in range(len(my_list)):
    int_list.append(int(my_list[index]))
sorted_int_list = list(int_list)
sorted_int_list.sort()
for num in range(numbers_remaining):
    int_list.remove(sorted_int_list[num])
str_list = [str(num) for num in int_list]
print(", ".join(str_list))