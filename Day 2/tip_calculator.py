#tip calculator - determines how much each person should pay based on the agreed on tip
# August 20, 2022
# 100 Days of Code Challenge
# Ivan Windon

print("Welcome to the tip calculator.")
total = input("What was the total bill? ")
tip = input("What percentage tip would you like to give? ")
people = input("How many people to split the bill? ")

bill = round((float(total) + (float(total) * (int(tip) / 100))) / int(people),2)

print(f"Each person should pay: ${bill}")