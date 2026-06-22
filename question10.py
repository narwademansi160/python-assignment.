def calculate_discount(price, discount_percent):
    discount = (price * discount_percent) / 100
    final_price = price - discount
    return final_price

price = float(input("Enter product price: "))
discount_percent = float(input("Enter discount percentage: "))

final_price = calculate_discount(price, discount_percent)

print("Discounted Price =", final_price)