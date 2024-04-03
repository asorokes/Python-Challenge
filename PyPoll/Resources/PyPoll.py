import os
import csv


 #Pathways
election_csv = "/Users/adamsorokes/Downloads/Starter_Code-17/PyPoll/Resources/election_data.csv"
output_text = "/Users/adamsorokes/Downloads/Starter_Code-17/PyPoll/Resources/election_analysis.txt"

# Creating Variables
num_votes = 0
received_votes = {}  # Use a dictionary to store votes for each candidate
candidates = set()   # Use a set to automatically keep track of unique candidates
percentage = {}

# Opening and reading the csv file
with open(election_csv) as csvfile:
    election_reader = csv.reader(csvfile, delimiter=',')
    csv_header = next(election_reader)  # Read the header row

    # Create lists for each category
    ballotid = []
    county = []
    candidate = []

    # Loop through rows with assigned variables
    for row in election_reader:
        ballotid.append(row[0])  # Append to the list, not overwrite
        county.append(row[1])
        candidate.append(row[2])

        # Count votes for each candidate
        if row[2] not in received_votes:
            received_votes[row[2]] = 1
        else:
            received_votes[row[2]] += 1

        # Keep track of unique candidates
        candidates.add(row[2])

        # Calculate the votes for each candidate
        num_votes += 1
        if row[2] not in received_votes:
            received_votes[row[2]] = 1
        else:
            received_votes[row[2]] += 1

# Calculate the number of total votes
total_votes = len(ballotid)

# Calculate the votes for each candidate and their percentage
for candidate_name in candidates:
    percentage[candidate_name] = (received_votes[candidate_name] / total_votes) * 100

# Calculate the candidate with the highest percentage of votes 
winner = max(percentage, key=percentage.get)

# Open the output file in write mode
with open('PyPoll.txt', 'w') as output_text:
    # Redirect the print output to the file
    print("Election Results", file=output_text)
    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _", file=output_text)
    print("Total Votes:", total_votes, file=output_text)
    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _", file=output_text)
    for candidate_name in candidates:
        print(f"{candidate_name}: {percentage[candidate_name]:.3f}% ({received_votes[candidate_name]})", file=output_text)
        print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _", file=output_text)
        print(f"Winner: {winner}", file=output_text)
        print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _", file=output_text)