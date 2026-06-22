n = int(input("Enter number of transactions:"))
deposit = 0
withdrawal = 0

for i in range(n):
    t = input("Enter D for Deposit or W for withdrawal:")
    
    if t.upper() =="D":
        deposit += 1
    elif t.upper() =="W":
        withdrawal += 1

print("Deposits =", deposit)
print("Withdrawals =", withdrawal)