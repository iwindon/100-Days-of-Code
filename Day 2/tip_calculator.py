print("Welcome to the tip calculator.")
total = input("What was the total bill? ")
percentage = input("What percentage tip would you like to give? ")
people = input("How many people to split the bill? ")

tip_as_percent = int(percentage) / 100
tip = float(total) * tip_as_percent
bill = round((float(total) + tip) / int(people),2)

print(f"Each person should pay: ${bill}")