# Write a program that reads four integer numbers. It should add the first to the second number, integer divide the
# sum by the third number, and multiply the result by the fourth number. Print the final result.

first_int = int(input())
second_int = int(input())
third_int = int(input())
fourth_int = int(input())
result = int((first_int + second_int) / third_int) * fourth_int
print(result)
