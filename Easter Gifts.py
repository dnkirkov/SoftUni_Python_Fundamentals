# As a good friend, you decide to buy presents for your friends.
# Create a program that helps you plan the gifts for your friends and family. First, you are going to
# receive the gifts you plan on buying on a single line, separated by space, in the following format:
# "{gift1} {gift2} {gift3}… {giftn}"
# Then you will start receiving commands until you read the "No Money" message. There are three possible
# commands:
# • "OutOfStock {gift}"
# o Find the gifts with this name in your collection, if any, and change their values to "None".
# • "Required {gift} {index}"
# o If the index is valid, replace the gift on the given index with the given gift.
# • "JustInCase {gift}"
# o Replace the value of your last gift with this one.
# In the end, print the gifts on a single line, except the ones with value "None", separated by a single space in the
# following format:
# "{gift1} {gift2} {gift3} … {giftn}"
# Input / Constraints
# • On the 1
# st line, you will receive the names of the gifts, separated by a single space.
# • On the following lines, until the "No Money" command is received, you will be receiving commands.
# • The input will always be valid.
# Output
# • Print the gifts in the format described above.

gifts = input().split()
flag = False
while 1:
    command = input()
    if "No Money" == command:
        flag = True
        break
    else:
        command_list = command.split()
    if flag:
        break
    elif "OutOfStock" == command_list[0]:
        for i in range(len(gifts)):
            if gifts[i] == command_list[1]:
                gifts[i] = "None"
    elif "Required" == command_list[0]:
        if int(command_list[2]) < len(gifts):
            gifts[int(command_list[2])] = command_list[1]
    elif "JustInCase" == command_list[0]:
        gifts[-1] = command_list[1]
while "None" in gifts:
    gifts.remove("None")
final_string = " ".join(gifts)
print(final_string)
