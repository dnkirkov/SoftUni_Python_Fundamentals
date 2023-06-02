# Write a function that receives a string and a counter n. The function should return a new string – the result of
# repeating the old string n times. Print the result of the function. Try using lambda.

repeat_string = lambda word, count: word * count
string = input()
counter = int(input())
print(repeat_string(string, counter))

