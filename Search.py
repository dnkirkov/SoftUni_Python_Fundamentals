# On the first line, you will receive a number n. On the second line, you will receive a word. On the following n lines,
# you will be given some strings. You should add them to a list and print them. After that, you should filter out only
# the strings that include the given word and print that list too

count = int(input())
keyword = input()
keyword_list = []
all_list = []
for i in range(count):
    string = input()
    if keyword in string:
        keyword_list.append(string)
        all_list.append(string)
    else:
        all_list.append(string)
print(all_list)
print(keyword_list)

