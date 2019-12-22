#import the os and csv modules
import os
import csv

#declare the path and open the csv for reading, and the output text path
PollCSV = os.path.join('PyPoll_CSV.csv')
OutputPoll = os.path.join('OutputPyPoll.txt')

with open(PollCSV, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

 #Declare Variables (use dictionaries and counters)
    Candidates = {}
    Count = 0
    Votes = 0
    percentVotes = 0 
    mostVotes = 0
    Winner = ""

    #go through each row of the csvfile
    for row in csvreader:
        #look into the candidates column; determine total votes and create candidate dict
        candidates = row[2]
        Count +=1
        if candidates in Candidates.keys():
            Candidates[candidates] +=1
        else:
            Candidates[candidates] = 1
    
    #create the outline of results and the total votes
    print("Election Results")
    print("-----------------------------")
    print(f"Total Votes: {Count}")
    print("-----------------------------")

    #determine total number of votes for each candidate
    for candidates in Candidates:
        Votes = Candidates[candidates]

        #determine percentage of votes
        percentVotes = (Candidates[candidates])/(Count)*100
        print(f"{candidates}: {int(percentVotes)}% ({Votes})")

        #find the most voted candidate
        if Candidates[candidates] > mostVotes:
            Winner = candidates
            mostVotes = Candidates[candidates]

    #print the remaining output table
    print("-----------------------------")
    print(f"Winner: {Winner}")
    print("-----------------------------")




##as mentioned in pyBank script, using variables and opening the 
##csvpath only once, to then perform all the functions,
##provides much cleaner and smaller code.  

with open (OutputPoll, 'w', newline='') as textfile:
    print("Election Results", file=textfile)
    print("----------------------------------", file=textfile)
    print(f"Total Votes: {Count}", file=textfile)
    print("-----------------------------", file=textfile)
    for candidates in Candidates:
        Votes = Candidates[candidates]
        percentVotes = (Candidates[candidates])/(Count)*100
        print(f"{candidates}: {int(percentVotes)}% ({Votes})", file=textfile)
    print("-----------------------------", file=textfile)
    print(f"Winner: {Winner}", file=textfile)
    print("-----------------------------", file=textfile)
   
