n = int(input("Enter number of days: "))
total = 0

for i in range(n):
    sale = int(input("Enter sale: "))
    total += sale

print("Total Sales =",total)    