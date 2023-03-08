# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

# days = 365
# weeks = 52
# months = 12

age_int = int(age)

years_left = 90 - age_int
days_left = 365 * years_left
weeks_left = 52 * years_left
months_left = 12 * years_left


message = f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left."
print(message)
