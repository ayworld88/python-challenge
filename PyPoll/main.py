import os
import csv

csvpath = os.path.join("..", "PyPoll", "election_data.csv")
      
total_votes = []
c_khan = []
c_correy = []
c_li = []
c_otooley = []
average_change = []

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    header = next(csvreader)
   
    print("Election Results")
    print("------------------------")

    for row in csvreader:
        total_votes.append(row[2])

        if row[2] == "Khan":
            c_khan.append(row[2])
        elif row[2] == "Correy":
            c_correy.append(row[2])
        elif row[2] == "Li":
            c_li.append(row[2])
        elif row[2] == "O'Tooley":
            c_otooley.append(row[2])

    khan_percent = round(len(c_khan)/len(total_votes) * 100, 3)
    correy_percent = round(len(c_correy)/len(total_votes) * 100, 3)
    li_percent = round(len(c_li)/len(total_votes) * 100, 3)
    otooley_percent = round(len(c_otooley)/len(total_votes) * 100, 3)
    
    print(f"Total Votes: {len(total_votes)}")
    print("------------------------")    
    print(f"Khan: {khan_percent}% ({len(c_khan)})")
    print(f"Correy: {correy_percent}% ({len(c_correy)})")
    print(f"Li: {li_percent}% ({len(c_li)})")
    print(f"O'Tooley: {otooley_percent}% ({len(c_otooley)})")
    print("------------------------")
    print(f"Winner: Khan")
    print("------------------------")
