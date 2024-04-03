import os
import csv
from pathlib import Path

# File pathways
input_path = "/Users/adamsorokes/Downloads/Starter_Code-17/PyBank/Resources/budget_data.csv"
output_text_path = "financial_analysis.txt"

# Variables
total_months = 0
total_profit = 0
previous_profit = 0
profit_changes = []
dates = []

# Print the data and calculate the totals
with open(input_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read header
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Print dates and calculate total
    for row in csvreader:
        total_months += 1
        profit = int(row[1])
        total_profit += profit
        if total_months > 1:  # Skip the first row as there is no previous profit for the first row
            profit_change = profit - previous_profit
            profit_changes.append(profit_change)
        dates.append(row[0])  # Date is in the first column
        previous_profit = profit

# Calculate average profit change
average_change = sum(profit_changes) / (total_months - 1)


#Calculate the highest increase in profits
biggest_increase = max(profit_changes)
biggest_decrease = min(profit_changes)

#Find the dates of the biggest increase and biggest loss
biggest_increase_date= dates[profit_changes.index(biggest_increase)]
biggest_decrease_date= dates[profit_changes.index(biggest_decrease)]

#Print final results to terminal
print("Financial Analysis")
print("_______________________________")
print(f"total months: {total_months}")
print(f"Total Profits: ${total_profit}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profit: {biggest_increase_date} (${biggest_increase})")
print(f"Greatest Decrease in Profits: {biggest_decrease_date} (${biggest_decrease})")