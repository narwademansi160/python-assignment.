def calculate_salary(salary, bonus):
    return salary + bonus

salary = float(input("Enter basic salary: "))
bonus = float(input("Enter bonus amount: "))

final_salary = calculate_salary(salary, bonus)

print("Final Salary =", final_salary)