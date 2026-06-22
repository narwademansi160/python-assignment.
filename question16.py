file = open("customers.txt", "w")

n = int(input("Enter number of customers: "))

for i in range(n):
    name = input("Enter customer name: ")
    file.write(name + "\n")

file.close()

print("Customer records saved successfully.")