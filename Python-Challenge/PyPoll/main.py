import csv
import os

#filepath = "Resources/budget_data.csv"
filepath = os.path.join("Resources", "election_data.csv")

total_ballots = 0
candidates = []
candidates_vote_count = []

with open(filepath, encoding='utf') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)    # Ballot ID, County, Candidate

    for row in csvreader:

        # Add row to total amount of ballots
        total_ballots += 1

        # Track all the candidates running
        if(len(candidates) == 0):                       # if this is the first iteration and candidates is empty
            candidates.append(row[2])
            candidates_vote_count.append(int(1))        # add first vote for the first candidate added
        else:                                           # loop through candidates list to check if name is already there
            name_not_found = True
            for x in candidates:
                if row[2] == x:
                    name_not_found = False
            if name_not_found:
                candidates.append(row[2])
                candidates_vote_count.append(int(1))    # add first vote for the newly added candidate
            else:
                for v in candidates:
                    if row[2] == v:
                        next
                        #candidates_vote_count[v-1] = int(candidates_vote_count[v-1]) - 1

            

    print(candidates_vote_count[0])
    print(type(candidates_vote_count[0]))
    print("Election Results\n")
    print("----------------\n")
    print(f"Total Votes: {total_ballots}\n")
    print("----------------\n")
    print(f"{candidates[0]}: {candidates_vote_count[0]}\n")
    print(f"{candidates[1]}: {candidates_vote_count[1]}\n")
    print(f"{candidates[2]}: {candidates_vote_count[2]}\n")
    print("----------------\n")
    print(f"Winner: {winner}")
    print("----------------\n")

    for x in candidates:
        print(x)                
        
        