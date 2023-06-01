# Write a program that receives a single string containing positive and negative numbers separated by a single space.
# Print a list containing the opposite of each number.

string = input()
my_list = list(string.split())
int_list = []
for i in range(len(my_list)):
    reverse_int = - int(my_list[i])
    int_list.append(reverse_int)
print(int_list)
