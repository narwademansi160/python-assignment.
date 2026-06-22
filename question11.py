try:
    amount = float(input("Enter payment amount: "))

    if amount <= 0:
        print("Invalid payment amount")
    else:
        print("Payment Successful:", amount)

except ValueError:
    print("Please enter a valid numeric amount")