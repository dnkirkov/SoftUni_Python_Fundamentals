# Write a program that receives a number n on the first line. On the following n lines, it receives different integer
# numbers. If the program receives an odd number, print "{num} is odd!" and end the program. Otherwise, if all
# numbers given are even, print "All numbers are even.".

even = True
counter = int(input())
for i in range(counter):
    number = int(input())
    if number % 2 != 0:
        even = False
        print(f"{number} is odd!")
        break
else:
    print("All numbers are even.")
