# You will be given strings until you receive the command "End". For each string given, you should print a string in
# which each character (case-sensitive) is repeated twice. Note that if you receive the string "SoftUni", you should
# NOT print it!

while 1:
    double_string = ''
    string = input()
    if string == "End":
        break
    elif string == "SoftUni":
        continue
    else:
        for i in range(len(string)):
            double_string += string[i] * 2
        print(double_string)
