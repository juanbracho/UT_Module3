#import the necesary modules
import csv
import os

# Path to the dataset
file_path = 'Resources/budget_data.csv'
analysis_dir = 'Analysis'
analysis_file = os.path.join(analysis_dir, 'financial_analysis.txt')

# Initialize variables
total_months = 0
net_total = 0
previous_profit_losses = None
changes = []
dates = []
greatest_increase = {"date": "", "amount": float('-inf')}
greatest_decrease = {"date": "", "amount": float('inf')}

# Read the dataset
with open(file_path, 'r') as file:
    reader = csv.reader(file)
    header = next(reader)  # Skip the header row
    
    for row in reader:
        date = row[0]
        profit_losses = int(row[1])
        
        # Calculate the total number of months
        total_months += 1
        
        # Calculate the net total amount of "Profit/Losses"
        net_total += profit_losses
        
        if previous_profit_losses is not None:
            change = profit_losses - previous_profit_losses
            changes.append(change)
            dates.append(date)
            
            # Check for greatest increase in profits
            if change > greatest_increase["amount"]:
                greatest_increase["date"] = date
                greatest_increase["amount"] = change
            
            # Check for greatest decrease in profits
            if change < greatest_decrease["amount"]:
                greatest_decrease["date"] = date
                greatest_decrease["amount"] = change
        
        previous_profit_losses = profit_losses

# Calculate the average change
average_change = sum(changes) / len(changes)

# Prepare the analysis results
analysis_results = [
    "Financial Analysis",
    "----------------------------",
    f"Total Months: {total_months}",
    f"Total: ${net_total}",
    f"Average Change: ${average_change:.2f}",
    f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})",
    f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})"
]

# Write the analysis results to a text file
with open(analysis_file, 'w') as file:
    for line in analysis_results:
        file.write(line + "\n")

# Print the analysis results
for line in analysis_results:
    print(line)