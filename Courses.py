# On the first line, you will receive a single number n. On the following n lines, you will receive names of courses.
# You should create a list of courses and print it.

courses_list = list()
number = int(input())
for i in range(number):
    course = input()
    courses_list.append(course)
print(courses_list)
