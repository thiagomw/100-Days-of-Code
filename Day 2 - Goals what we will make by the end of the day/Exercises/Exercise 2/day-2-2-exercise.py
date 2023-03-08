# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

new_weight = float(weight)
new_height = float(height)

bmi = new_weight / (new_height * new_height)
bmi_int = int(bmi)

print("Your BMI is:", bmi_int)
