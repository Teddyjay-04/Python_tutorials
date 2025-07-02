#Week 1 project
# This program collects and formats user info

# Asking for user input
name = input("Enter your full name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height in meters: "))
is_student = input("Are you a student? (yes/no): ").lower() == "yes"

# Simple calculation
years_until_30 = 30 - age

# Boolean logic to check age group
is_minor = age < 18

# Output formatting
print("\n===== PROFILE SUMMARY =====")
print(f"Name: {name.title()}")
print(f"Age: {age} years old")
print(f"Height: {height} meters")
print(f"Student Status: {'Yes' if is_student else 'No'}")
print(f"Years until 30: {years_until_30}")

if is_minor:
    print("Status: You are still a minor.")
else:
    print("Status: You are an adult.")
