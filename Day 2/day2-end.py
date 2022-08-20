# num_char = len(input("What is your name: "))

# new_num_char = str(num_char)

# print("Your name has " + new_num_char + " characters.")

# print(type(num_char))

# a = str(123)
# b = 123
# c = float(123)
# print(type(a))
# print(type(b))
# print(type(c))

# print(70 + float(100.75))

# two_digit_number = input("Type a two digit number: ")
# numbers = str(two_digit_number)
# print(int(numbers[0]) + int(numbers[1]))

# print(3 * (3 + 3) / 3 - 3)


# print("BMI Calculator")
# height = input("enter your height in m: ")
# weight = input("enter your weight in kg: ")
# print(type(height))
# print(type(weight))
# bmi_height = float(height)
# bmi_weight = float(weight)
# print(type(bmi_height))
# print(type(bmi_weight))
# bmi = bmi_weight / bmi_height ** 2
# print(f"Your BMI is: {int(bmi)}")


age = input("What is your current age?")


years_lifetime = 90

years_remaining = 90 - int(age)
months_remaining = years_remaining * 12
weeks_remaining = years_remaining * 52
days_remaining = years_remaining * 365

print(f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left.")
