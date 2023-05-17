# You will be given two strings. Transform the first string into the second one letter by letter starting from the first
# one. After each interaction, print the resulting string only if it is unique.
# Note: the strings will have the same length.

first_string = input()
second_string = input()
last_string = ""
for i in range(len(first_string)):
    left_part = second_string[:i + 1]
    right_part = first_string[i + 1:]
    current_string = left_part + right_part
    if current_string == last_string:
        continue
    else:
        print(current_string)
        last_string = current_string
