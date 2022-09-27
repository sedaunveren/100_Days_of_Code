# print("Hello"[4])


#score = 0
#height = 1.8
#isWinning = True
#f-String
#print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")


print("Welcome to the tip calculator.")
bill = float(input("What is the total bill?  $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? ")) 
people = int(input("How many people to split the bill?"))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: ${final_amount}")  