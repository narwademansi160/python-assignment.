try:
    age = int(input("Enter your age: "))

    if age >= 18:
        print("Eligible")
    else:
        print("Not Eligible")

except ValueError:
    print("Error: Please enter a valid numeric age")