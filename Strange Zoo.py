# You are at the zoo, and the meerkats look strange.
# You will receive 3 strings on separate lines, representing the tail, the body, and the head of an animal in that order
# Your task is to re-arrange the elements in a list so that the animal looks normal again:
# • On the first position is the head;
# • On the second position is the body;
# • On the last one is the tail.

animal_list = list()
for part in range(3):
    data = input()
    animal_list.append(data)

animal_list[0], animal_list[2] = animal_list[2], animal_list[0]
print(animal_list)
