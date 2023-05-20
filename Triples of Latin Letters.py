# Write a program to read an integer N and print all triples of the first N small Latin letters, ordered alphabetically

number_of_letters = int(input())
for a in range(number_of_letters):
    for b in range(number_of_letters):
        for c in range(number_of_letters):
            print(f"{chr(a + 97)}{chr(b + 97)}{chr(c + 97)}")
