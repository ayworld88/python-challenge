import os
import csv

csvpath = os.path.join("..", "PyBank", "budget_data.csv")
      
months = []
profit_losses = []
average_change = []

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    header = next(csvreader)
   
    print("Financial Analysis")
    print("------------------------")

    for row in csvreader:
        months.append(row[0])
        profit_losses.append(int(row[1]))
    
    print(f"Total Months: {len(months)}")
    print(f"Total: {sum(profit_losses)}")
    
    for i in range(1, len(profit_losses)):
        average_change.append(profit_losses[i] - profit_losses[i-1])
        pl_change = round(sum(average_change)/len(average_change), 2)
        
        max_profit = max(average_change)
        min_profit = min(average_change)

        max_profit_date = str(months[average_change.index(max(average_change)) +1])
        min_profit_date = str(months[average_change.index(min(average_change)) +1])

    print(f"Average Change: $ {pl_change}")
    print(f"Greatest Increase in Profits: {max_profit_date} ({max_profit})")
    print(f"Greatest Decrease in Profits: {min_profit_date} ({min_profit})")
