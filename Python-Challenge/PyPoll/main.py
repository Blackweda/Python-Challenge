import csv
import os


#filepath = "Resources/budget_data.csv"
filepath = os.path.join("Resources", "election_data.csv")

total_ballots = 0
candidates = []
candidates_vote_count = []
winner = ""

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
                for v in candidates:                    # look up the list of votes that matches the candidate
                    if row[2] == v:
                        current_count = candidates_vote_count[candidates.index(v)]
                        current_count += 1
                        candidates_vote_count[candidates.index(v)] = current_count


    print("Election Results\n")
    print("----------------\n")
    print(f"Total Votes: {total_ballots}\n")
    print("----------------\n")
    print(f"{candidates[0]}: {round((candidates_vote_count[0]/total_ballots)*100, 3)}% ({candidates_vote_count[0]})\n")
    print(f"{candidates[1]}: {round((candidates_vote_count[1]/total_ballots)*100, 3)}% ({candidates_vote_count[1]})\n")
    print(f"{candidates[2]}: {round((candidates_vote_count[2]/total_ballots)*100, 3)}% ({candidates_vote_count[2]})\n")
    print("----------------\n")
    print(f"Winner: {candidates[candidates_vote_count.index(max(candidates_vote_count))]}\n")
    print("----------------\n")

    # Write information to an Analysis folder
    analysis_file = os.path.join("Analysis", "election_data_analysis.txt")
    
    with open(analysis_file, "w") as datafile:

        tb = repr(total_ballots)

        c1va = repr(round((candidates_vote_count[0]/total_ballots)*100, 3))
        c1v = repr(candidates_vote_count[0])
        
        c2va = repr(round((candidates_vote_count[1]/total_ballots)*100, 3))
        c2v = repr(candidates_vote_count[1])
        
        c3va = repr(round((candidates_vote_count[2]/total_ballots)*100, 3))
        c3v = repr(candidates_vote_count[2])

        winner = repr(candidates[candidates_vote_count.index(max(candidates_vote_count))])

        
        
        analysis = "\
Election Results\n\
------------------\n\
Total Votes: " + tb + "\n\
------------------\n\
" + candidates[0] + ": " + c1va + "% (" + c1v + ")\n\
" + candidates[1] + ": " + c2va + "% (" + c2v + ")\n\
" + candidates[2] + ": " + c3va + "% (" + c3v + ")\n\
------------------\n\
Winner: " + winner + "\n\
------------------"

        datafile.write(analysis)

        datafile.close             
        
        