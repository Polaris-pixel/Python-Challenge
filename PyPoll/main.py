import os
import csv

poll_path = os.path.join("Resources","election_data.csv")

with open (poll_path, 'r') as poll_file:
    poll_data=csv.reader(poll_file, delimiter=',')
    #print (poll_data)
    
    poll_header = next(poll_data)
    #print (f"Data Header: {poll_header}")
    total_votes=0
    candidates = []
    candidates_votes =[]
    for row in poll_data:
        #print(row)
        total_votes += 1
        if row[2] not in candidates:
            candidates.append(row[2])
            candidates_votes.append(0)
            
    
        candidates_votes[candidates.index(row[2])] += 1
        
    percentage_votes = []
    for x in candidates:
        
        percentage = (candidates_votes[candidates.index(x)]/total_votes) * 100
        percentage_votes.append(percentage)
        
    
            
        
                
        
        
        
print(total_votes)   
print(candidates)
print(candidates_votes)
print(percentage_votes)

# Election Results
#   -------------------------
#   Total Votes: 3521001
#   -------------------------
#   Khan: 63.000% (2218231)
#   Correy: 20.000% (704200)
#   Li: 14.000% (492940)
#   O'Tooley: 3.000% (105630)
#   -------------------------
#   Winner: Khan
#   -------------------------
