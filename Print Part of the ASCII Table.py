# Write a program that prints part of the ASCII table characters on the console, separated by a single space. On the
# first line of input, you will receive the char index you should start with. On the second line - the index of the last
# character you should print.

first_num = int(input())
second_num = int(input())
final_string = ""
for i in range(first_num, second_num + 1):
    final_string += chr(i) + " "
print(final_string)
