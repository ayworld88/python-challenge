# import dependencies
import os
import csv

csvpath = os.path.join("..", "PyBank", "budget_data.csv")

# create lists to store files    
months = []
profit_losses = []
average_change = []

# Set path for file
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

# skip header
    header = next(csvreader)
   
    
# iterate through rows to retrieve data to store in the empty lists above 
    for row in csvreader:
        months.append(row[0])
        profit_losses.append(int(row[1]))
    
    
  # run second loop for calculations  
    for i in range(1, len(profit_losses)):
        average_change.append(profit_losses[i] - profit_losses[i-1])
        pl_change = round(sum(average_change)/len(average_change), 2)
        
        max_profit = max(average_change)
        min_profit = min(average_change)

        max_profit_date = str(months[average_change.index(max(average_change)) +1])
        min_profit_date = str(months[average_change.index(min(average_change)) +1])

# print statements
    print("Financial Analysis")
    print("------------------------")
    print(f"Total Months: {len(months)}")
    print(f"Total: {sum(profit_losses)}")
    print(f"Average Change: $ {pl_change}")
    print(f"Greatest Increase in Profits: {max_profit_date} ({max_profit})")
    print(f"Greatest Decrease in Profits: {min_profit_date} ({min_profit})")

# write print statements to text file
f = open("PyBank.txt","w+")  
f.write("Financial Analysis\n")
f.write("------------------------\n")
f.write(f"Total Months: {len(months)}\n")
f.write(f"Total: {sum(profit_losses)}\n")
f.write(f"Average Change: $ {pl_change}\n")
f.write(f"Greatest Increase in Profits: {max_profit_date} ({max_profit})\n")
f.write(f"Greatest Decrease in Profits: {min_profit_date} ({min_profit})\n")
f.close()