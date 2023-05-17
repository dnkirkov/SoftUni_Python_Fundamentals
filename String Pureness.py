# You will be given number n. After that, you'll receive different strings n times. Your task is to check if the given
# strings are pure, meaning that they do NOT consist of any of the characters: comma ",", period ".", or underscore "_":
# • If a string is pure, print "{string} is pure."
# • Otherwise, print "{string} is not pure!"

number_of_strings = int(input())
flag = False
for a in range(number_of_strings):
    string = input()
    for b in range(len(string)):
        if string[b] in [",", ".", "_"]:
            print(f"{string} is not pure!")
            flag = True
            break
        else:
            flag = False
    if not flag:
        print(f"{string} is pure.")
