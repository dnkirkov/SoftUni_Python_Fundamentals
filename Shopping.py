# Write a program that reads an integer number representing a budget. On the following lines, it reads integer
# numbers representing the prices of each product you should buy until it receives the command "End".
# During the iterations, if there is not enough budget left to buy the next product, it prints "You went in
# overdraft!" and end the program.
# Otherwise, if you accomplished to buy all products before receiving "End", it prints "You bought everything
# needed."

budget = float(input())
cost = 0
product_cost = str
while True:
    product_cost = input()
    if product_cost == "End":
        print("You bought everything needed.")
        break
    else:
        product_cost = float(product_cost)
    cost += product_cost
    if cost > budget:
        print("You went in overdraft!")
        break

