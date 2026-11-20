# CSV-Based Payroll Management System

import csv
import os

FILENAME = "payroll.csv"

def add_employee():
    emp_id = input("Enter employee ID: ")
    name = input("Enter employee name: ")
    hours = float(input("Enter hours worked: "))
    rate = float(input("Enter hourly pay rate: "))
    gross_pay = hours * rate

    file_exists = os.path.exists(FILENAME)
    with open(FILENAME, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Employee ID", "Name", "Hours", "Hourly Rate", "Gross Pay"])
        writer.writerow([emp_id, name, hours, rate, gross_pay])

    print("Payroll record saved. Gross pay:", round(gross_pay, 2))

def view_payroll():
    try:
        with open(FILENAME, "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            for row in reader:
                print(" | ".join(row))
    except FileNotFoundError:
        print("No payroll records found.")

while True:
    print("\n--- Payroll Management ---")
    print("1. Add employee payroll")
    print("2. View payroll")
    print("3. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        add_employee()
    elif choice == "2":
        view_payroll()
    elif choice == "3":
        print("Exiting payroll system.")
        break
    else:
        print("Invalid choice.")

output

--- Payroll Management ---
1. Add employee payroll
2. View payroll
3. Exit
Enter choice: 1
Enter employee ID: 12567
Enter employee name: sai
Enter hours worked: 67
Enter hourly pay rate: 87
Payroll record saved. Gross pay: 5829.0

--- Payroll Management ---
1. Add employee payroll
2. View payroll
3. Exit
Enter choice: 2
Employee ID | Name | Hours | Hourly Rate | Gross Pay
12567 | sai | 67.0 | 87.0 | 5829.0

--- Payroll Management ---
1. Add employee payroll
2. View payroll
3. Exit
Enter choice: 3
Exiting payroll system.
