# import dependencies
import os
import csv

# set path for file source
csvpath = os.path.join("..", "PyPoll", "election_data.csv")

# create lists to store files        
total_votes = []
c_khan = []
c_correy = []
c_li = []
c_otooley = []
average_change = []

# open csv file
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

# skip header
    header = next(csvreader)
   
    
# iterate through rows to retrieve data to store in the empty lists above 
    for row in csvreader:
        total_votes.append(row[2])


# tally up total votes for each candidates by looping over entire row and add to empty lists
        if row[2] == "Khan":
            c_khan.append(row[2])
        elif row[2] == "Correy":
            c_correy.append(row[2])
        elif row[2] == "Li":
            c_li.append(row[2])
        elif row[2] == "O'Tooley":
            c_otooley.append(row[2])

# convert each candidates votes to percentages of total votes
    khan_percent = round(len(c_khan)/len(total_votes) * 100, 3)
    correy_percent = round(len(c_correy)/len(total_votes) * 100, 3)
    li_percent = round(len(c_li)/len(total_votes) * 100, 3)
    otooley_percent = round(len(c_otooley)/len(total_votes) * 100, 3)

# get winner  
    percent_list = [khan_percent, correy_percent, li_percent, otooley_percent]
    maximum = max(percent_list)
    if khan_percent == maximum:
        winner = "Khan"
    if correy_percent == maximum:
        winner = "Correy"
    if li_percent == maximum:
        winner = "Li"
    if otooley_percent == maximum:
        winner = "O'Tooley"

  # print statements  
    print("Election Results")
    print("------------------------")
    print(f"Total Votes: {len(total_votes)}")
    print("------------------------")    
    print(f"Khan: {khan_percent}% ({len(c_khan)})")
    print(f"Correy: {correy_percent}% ({len(c_correy)})")
    print(f"Li: {li_percent}% ({len(c_li)})")
    print(f"O'Tooley: {otooley_percent}% ({len(c_otooley)})")
    print("------------------------")
    print(f"Winner: {winner}")
    print("------------------------")

# write print statements to text file
f = open("PyPoll.txt", "w+")
f.write("Election Results\n")
f.write("------------------------\n")
f.write(f"Total Votes: {len(total_votes)}\n")
f.write("------------------------\n")    
f.write(f"Khan: {khan_percent}% ({len(c_khan)})\n")
f.write(f"Correy: {correy_percent}% ({len(c_correy)})\n")
f.write(f"Li: {li_percent}% ({len(c_li)})\n")
f.write(f"O'Tooley: {otooley_percent}% ({len(c_otooley)})\n")
f.write("------------------------\n")
f.write(f"Winner: {winner}\n")
f.write("------------------------\n")
f.close()
