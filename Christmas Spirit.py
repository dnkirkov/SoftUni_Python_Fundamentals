# It is time to get in a Christmas mood. You need to decorate the house in time for the big event, but you have limited
# days to do so.
# Write a program that calculates how much money you will need to spend on Christmas decorations and how much
# your Christmas spirit will improve.
# On the first line, you will receive the quantity of decorations you should buy each time you go shopping.
# On the second line, you will receive the days left until Christmas.
# There are 4 types of decorations, and each piece costs a certain price. Also, each time you go shopping for a concrete
# type of decoration, your Christmas spirit is improved by some points:
# Decoration Price/Piece Points/Shopping
# Ornament Set 2$ 5
# Tree Skirt 5$ 3
# Tree Garland 3$ 10
# Tree Lights 15$ 17
# Until Christmas, you go shopping for a certain decoration as follows:
# • Every second day you buy Ornament Sets.
# • Every third day you buy Tree Skirts and Tree Garlands.
# • Every fifth day you buy Tree Lights.
# o If you have bought Tree Skirts and Tree Garlands on the same day, you additionally increase your
# spirit by 30.
# Hint: A day happens to be the third one as well as the fifth one at the same time (for example the 15th day).
# That's not all! You have a cat at home that really likes to mess around with the decoration:
# • Every tenth day your cat ruins all tree decorations, and you lose 20 points of the spirit:
# o Because of that, you go shopping (for a second time during the day) to buy one piece of tree skirt,
# garlands, and lights, but you do NOT earn additional spirit points for them.
# • Also, because of the cat - at the beginning of every eleventh day, you are forced to increase the quantity of
# decorations needed to be bought each time you go shopping by adding 2.
# • If the last day is a tenth day, the cat demolishes even more and ruins the Christmas turkey, and you lose an
# additional 30 points of spirit.
# In the end, you must print the total cost and the gained spirit.
# Input / Constraints
# The input will consist of exactly 2 lines:
# • quantity - integer in the range [1…100]
# • days - integer in the range [1…100]
# Output
# In the end, print the total cost and the total gained spirit in the following format:
# • "Total cost: {budget}"
# • "Total spirit: {totalSpirit}"

number_of_decorations_per_day = int(input())
days_until_christmas = int(input())
cost = 0
spirit = 0
for i in range(1, days_until_christmas + 1):
    if i % 11 == 0:
        number_of_decorations_per_day += 2
    if i % 10 == 0:
        spirit -= 20
        cost += 5 + 3 + 15
    if i % 5 == 0:
        cost += 15 * number_of_decorations_per_day
        spirit += 17
        if i % 3 == 0:
            spirit += 30
    if i % 3 == 0:
        cost += (5 + 3) * number_of_decorations_per_day
        spirit += 3 + 10
    if i % 2 == 0:
        cost += 2 * number_of_decorations_per_day
        spirit += 5
if days_until_christmas % 10 == 0:
    spirit -= 30
print(f"Total cost: {cost}")
print(f"Total spirit: {spirit}")
