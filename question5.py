n = int(input("Enter number of days: "))
threshold = int(input("Enter unit threshold: "))

count = 0

for i in range(n):
    units = int(input(f"Enter units for day {i+1}: "))

    if units > threshold:
        count += 1

print("Days crossed threshold:", count)