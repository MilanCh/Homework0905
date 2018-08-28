# import and read
import os
import csv
csvpath = os.path.join("budget_data.csv")
with open(csvpath, newline="") as budgetfile:
    csvreader = csv.reader(budgetfile, delimiter=",")
    csv_header = next(csvreader)


# The total net amount of "Profit/Losses" 
def total(sum):  
    total = 0
    for row in csvreader:
        total = total + int(row[1])
    return total
print(total(row[1]))

# The total number of months
Total_Months = sum(1 for line in open("budget_data.csv")) -1
print(Total_Months)


