def check_password(password):
    if len(password) >= 8:
        return "Password is Acceptable"
    else:
        return "Password is Not Acceptable"

password = input("Enter Password: ")

result = check_password(password)

print(result)