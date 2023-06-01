# The group of adventurists has gone on their first task. Now they should walk through fire - literally.
# They should use all the water they have left. Your task is to help them survive.
# Create a program that calculates the water needed to put out a "fire cell", based on the given information about its
# "fire level" and how much it gets affected by water.
# First, you will be given the level of fire inside the cell with the integer value of the cell,
# which represents the needed water to put out the fire. They will be given in the following format:
# "{typeOfFire} = {valueOfCell}#{typeOfFire} = {valueOfCell}# … {typeOfFire} =
# {valueOfCell}
# Afterward you will receive the amount of water you have for putting out the fires. There is a range of fire for each
# fire type, and if a cell's value is below or exceeds it, it is invalid, and you do not need to put it out.
# Type of Fire Range
# High 81 - 125
# Medium 51 - 80
# Low 1 - 50
# If a cell is valid, you should put it out by reducing the water with its value.
# Putting out fire also takes effort, and you need to calculate it.
# Its value is equal to 25% of the cell's value. In the end,
# you will have to print the total effort. Keep putting out cells until you run out of water.
# Skip it and try the next one if you do not have enough water to put out a
# given cell. In the end, print the cells you have put out in the following format:
# "Cells:
# - {cell1}
# - {cell2}
# …
# - {cellN}"
# "Effort: {effort}"
# The effort should be formatted to the second decimal place.
# In the end, print the total fire you have put out from all the cells in the following format:
# "Total Fire: {total_fire}"
# Input / Constraints
# • On the 1st line, you will receive the fires with their cells in the format described above – integer numbers in the
# range [1…500].
# • On the 2nd line, you will receive the water – an integer number in the range [0….100000].
# Output
# Print the output as described above.

total_fires_list = input().split("#")
total_water = int(input())
total_effort = 0
total_fire = 0
fire_cells = []
fire_list_list = []
invalid_fires = []
for fire in total_fires_list:
    fire_list = fire.split(" = ")
    fire_list[1] = int(fire_list[1])
    fire_list_list.append(fire_list)
for command in fire_list_list:
    if command[0] == "High":
        if command[1] < 81 or command[1] > 125:
            invalid_fires.append(command)
    elif command[0] == "Medium":
        if command[1] < 51 or command[1] > 80:
            invalid_fires.append(command)
    elif command[0] == "Low":
        if command[1] < 1 or command[1] > 50:
            invalid_fires.append(command)
for str in invalid_fires:
    fire_list_list.remove(str)
for fire in fire_list_list:
    if fire[1] > total_water:
        pass
    else:
        total_water -= fire[1]
        total_fire += fire[1]
        total_effort += fire[1] * 0.25
        fire_cells.append(fire[1])
print("Cells:")
for cell in fire_cells:
    print(f"- {cell}")
print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {total_fire}")

