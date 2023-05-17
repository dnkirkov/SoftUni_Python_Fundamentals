# You work at a coffee shop, and your job is to place orders to the distributors. Thus, you want to know the price of
# each order. On the first line, you will receive integer N - the number of orders the shop will receive. For each order
# you will receive the following information:
# • Price per capsule - a floating-point number in the range [0.01…100.00]
# • Days - integer in the range [1…31]
# • Capsules, needed per day - integer in the range [1…2000]
# For each order, you should print a single line in the following format:
# • "The price for the coffee is: ${price}"
# If you do not receive a correct order (one or more of the values are not in the given range), you should ignore it and
# move to the next one.
# After you go through all orders, you need to print the total price in the following format:
# • "Total: ${total_price}"
# Both the price of a coffee and the total price must be formatted to the second decimal place.

number_of_orders = int(input())
total_order_price = 0
for i in range(number_of_orders):
    price_per_capsule = float(input())
    days_order = int(input())
    capsules_per_day = int(input())
    price_per_order = price_per_capsule * capsules_per_day * days_order
    if price_per_order > 0:
        print(f"The price for the coffee is: ${price_per_order:.2f}")
    total_order_price += price_per_order
print(f"Total: ${total_order_price:.2f}")
