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
                
# print(total_votes)   
# print(candidates)
# print(candidates_votes)
# print(percentage_votes)


print ("Election Results")
print ("------------------------------")
print (f"Total Votes: {total_votes:0,.0f}")
print ("-------------------------------")

output_path = os.path.join("Analysis", "Summary_PyPoll.txt")


with open(output_path, 'w') as pollfile: 
      
    pollfile.write('Election Results \n')    
    pollfile.write('---------------------------------------- \n')
    pollfile.write(f"Total votes :  {total_votes:0,.0f}  \n" )
    pollfile.write('---------------------------------------- \n')
    for x in candidates:
        ind = candidates.index(x)
        votes = candidates_votes[ind]
        print (f"{(x)} : {(percentage_votes[ind]):0,.3f}% ({votes:0,.0f})")
        pollfile.write(f"{(x)} :  {(percentage_votes[ind]):0,.3f}%  ({votes:0,.0f}) \n")
    pollfile.write("--------------------------------------- \n")
    pollfile.write(f"Winner: {candidates[candidates_votes.index(max(candidates_votes))]} \n")
    pollfile.write("----------------------------------------")

print ("--------------------------------")
print (f"Winner: {candidates[candidates_votes.index(max(candidates_votes))]}")   
print ("-------------------------------")



    