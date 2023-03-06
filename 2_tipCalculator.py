# this is Tip calcatort program
#Take the billfrom the user and split the bill into person want to split he bill
#
print("Welcome to the tip calculator.")
bill =float(input("What was the total bill?"))
tip =int(input("What percentage of tip would you like 10,12 or 15?"))
split =int(input("How many people will split the bill?"))
#This is the percentage of tip 
percnt_Tip=tip/100
#This is Tip bill
Tip_bill=bill*percnt_Tip
#This is bill splited between the persons 
split_bill=bill/split
#Total bill should be bill splited + tip bill
Total_bill=Tip_bill+split_bill
#Final bill should  be rounded to 2 decimal places
final_Bill=round(Total_bill,2)

print(f"Your bill splited per person is{final_Bill}")

