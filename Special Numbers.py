# Write a program that reads an integer n. Then, for all numbers in the range [1, n],
# prints the number and if it is special or not (True / False).
# A number is special when the sum of its digits is 5, 7, or 11.

number_input = int(input())
for num in range(1, number_input + 1):
    sum_of_numbers = 0
    digits = num
    while digits > 0:
        sum_of_numbers += digits % 10
        digits = int(digits / 10)
    if sum_of_numbers in [5, 7, 11]:
        print(f"{num} -> True")
    else:
        print(f"{num} -> False")