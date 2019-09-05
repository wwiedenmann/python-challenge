import os
import csv

election_data = os.path.join("election_data.csv")

# Creat a list to keep track of the candidates
candidates_list = []

# Create a list to keep track of the number of votes per candidate 
num_votes_list = []

# Create a list to keep track of the percentage of total votes each candidate gets 
percent_votes = []

# Establish a counter for each vote 
votes_counter = 0

with open(election_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)

    for row in csvreader:
        # Add to our vote-counter 
        votes_counter += 1 

        '''
        If the candidate is not on our list, add his/her name to our list, along with 
        a vote in his/her name.
        If he/she is already on our list, we will simply add a vote in his/her
        name 
        '''
        if row[2] not in candidates_list:
            candidates_list.append(row[2])
            index = candidates_list.index(row[2])
            num_votes_list.append(1)
        else:
            index = candidates_list.index(row[2])
            num_votes_list[index] += 1
    
    # Add to percent_votes list 
    for votes in num_votes_list:
        percentage = (votes/votes_counter) * 100
        percentage = round(percentage)
        percentage = "%.3f%%" % percentage
        percent_votes.append(percentage)
    
    # Find the winning candidate
    winner = max(num_votes_list)
    index = num_votes_list.index(winner)
    winning_candidate = candidates_list[index]

# Displaying results
print("Election Results")
print("--------------------------")
print(f"Total Votes: {str(votes_counter)}")
print("--------------------------")
for i in range(len(candidates_list)):
    print(f"{candidates_list[i]}: {str(percent_votes[i])} ({str(num_votes_list[i])})")
print("--------------------------")
print(f"Winner: {winning_candidate}")
print("--------------------------")

# Exporting to .txt file
output = open("output.txt", "w")
line1 = "Election Results"
line2 = "--------------------------"
line3 = str(f"Total Votes: {str(votes_counter)}")
line4 = str("--------------------------")
output.write('{}\n{}\n{}\n{}\n'.format(line1, line2, line3, line4))
for i in range(len(candidates_list)):
    line = str(f"{candidates_list[i]}: {str(percent_votes[i])} ({str(num_votes_list[i])})")
    output.write('{}\n'.format(line))
line5 = "--------------------------"
line6 = str(f"Winner: {winning_candidate}")
line7 = "--------------------------"
output.write('{}\n{}\n{}\n'.format(line5, line6, line7))

