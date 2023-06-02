# Write a function that calculates the total price of an order and returns it. The function should receive one of the
# following products: "coffee", "coke", "water", or "snacks", and a quantity of the product. The prices for a
# single piece of each product are:
# • coffee - 1.50
# • water - 1.00
# • coke - 1.40
# • snacks - 2.00
# Print the result formatted to the second decimal place

def calculate_price(product, qty):
    products = ["coffee", "coke", "water", "snacks"]
    if product == products[0]:
        return f"{qty * 1.5:.2f}"
    elif product == products[1]:
        return f"{qty * 1.4:.2f}"
    elif product == products[2]:
        return f"{qty * 1:.2f}"
    elif product == products[3]:
        return f"{qty * 2:.2f}"


item = input()
quantity = int(input())
print(calculate_price(item, quantity))
