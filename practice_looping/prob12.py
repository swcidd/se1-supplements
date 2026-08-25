##Write a function named calculate_total(price, quantity, is_member) that calculates the total cost of a coffee order.
##If the user buys 3 or more coffees, they get a 10% discount on the entire order.
##If they are a member (is_member = True), they get an additional 5% discount (applied after the bulk discount).
##Return the final total price rounded to 2 decimal places

def calculate_total(price, quantity, is_member):
    total = price * quantity

    if quantity >= 3:
        total *= 0.90

    if is_member:
        total *= 0.95

    return round(total, 2)


print(calculate_total(4.00, 2, False))
print(calculate_total(4.00, 3, False))
print(calculate_total(4.00, 3, True))