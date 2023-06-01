# You want to go to France by train, and the train ticket costs exactly 150$. You do not have enough money, so you
# decide to buy some items with your budget and then sell them at a higher price – with a 40% markup.
# You will receive a collection of items and a budget in the following format:
# {type->price|type->price|type->price……|type->price}
# {budget}
# The prices for each of the types cannot exceed a specific price, which is given below:
# Type Maximum Price
# Clothes 50.00
# Shoes 35.00
# Accessories 20.50
# If a price for a particular item is higher than the maximum price, don't buy it. Every time you buy an item, you have
# to reduce the budget with its price value. If you don't have enough money for it, you can't buy it. Buy as many items
# as you can.
# Next, you should increase the price of each item you have successfully bought by 40% and then sell it. Calculate if
# the budget after selling all the items is enough for buying the train ticket.
# Input / Constraints
# • On the 1st line, you will receive the items with their prices in the format described above – real numbers in the
# range [0.00……1000.00]
# • On the 2nd line, you are going to be given the budget – a real number in the range [0.0….1000.0]
# Output
# • First, print the list with the bought item’s new prices, formatted to the second decimal point in the following
# format:
# "{price1} {price2} {price3} … {priceN}"
# • Second, print the profit, formatted to the second decimal point in the following format:
# "Profit: {profit}"
# • Finally:
# o If the budget is enough for buying the train ticket, print: "Hello, France!"
# o Otherwise, print: "Not enough money."

shopping_list = input().split("|")
shopping_list_list = []
invalid_objects = []
bought_items = []
new_price_items = []
budget = float(input())
starting_budget = budget
#Clothes->43.30|Shoes->25.25|Clothes->36.52|Clothes->20.90|Accessories->15.60
for item in shopping_list:
    item = item.split("->")
    item[1] = float(item[1])
    shopping_list_list.append(item)
for object in shopping_list_list:
    if object[0] == "Clothes":
        if object[1] > 50:
            invalid_objects.append(object)
        elif object[1] < budget:
            budget -= object[1]
            bought_items.append(object[1])
    elif object[0] == "Shoes":
        if object[1] > 35:
            invalid_objects.append(object)
        elif object[1] < budget:
            budget -= object[1]
            bought_items.append(object[1])
    elif object[0] == "Accessories":
        if object[1] > 20.5:
            invalid_objects.append(object)
        elif object[1] < budget:
            budget -= object[1]
            bought_items.append(object[1])
for remove in invalid_objects:
    shopping_list_list.remove(remove)
for index in bought_items:
    element = index * 1.4
    budget += element
    new_price_items.append(element)
for price in new_price_items:
    print(f"{price:.2f}", end=" ")
profit = budget - starting_budget
print()
print(f"Profit: {profit:.2f}")
if budget > 150:
    print("Hello, France!")
else:
    print("Not enough money.")
