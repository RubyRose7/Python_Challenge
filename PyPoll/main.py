import os
import csv 

newpath = os.path.join('Resources', 'pypoll-data.txt')

#To assign variables
voter_id= []
county=[]
candidate= []
total_votes= 0
total_candidates= []
perc_candidate= []
winner= []
election_data= []
candidate_votes= []

#To create CSV Path 
csvpath= os.path.join('Resources', 'Pypoll_Resources_election_data.csv')

#To Read CSV file
with open (csvpath) as csvfile:
	csvreader= csv.reader(csvfile, delimiter= ',')
	header= next (csvreader)
	
	

# To find total number of votes cast 
	for row in csvreader:
		total_votes= total_votes + 1

	# To To find total number of candidates who received votes
		if candidate.count(row[2]) == 0:
			candidate.append(row[2]) 
			candidate_votes.append(1)
		else:
			candidate_index= candidate.index(row[2]) 
			candidate_votes[candidate_index]= candidate_votes[candidate_index] + 1
	perc_candidate= [x/total_votes for x in candidate_votes]
	percentvote =["{0:.3%}".format(round((z), 3)) for z in perc_candidate]

	winner= 0
	for i in candidate:
		index1= candidate.index(i)
		if candidate_votes[index1] > winner:
			winner= candidate_votes[index1]

	index2= candidate_votes.index(winner)
print(winner)
print(candidate[index2])

	#print(perc_candidate)
	#print(percentvote)


print(candidate_votes)
print(candidate)



	# Percebntage of votes each candidate won
  



# Winner of election based on popular vote 


# To print results 
with open (newpath, 'w') as textfile:
		print(f'Election Results\n-----------------------------------\ntotal_votes: {candidate_votes}\n-----------------------------------')	
		textfile.write(f'Election Results\n-----------------------------------\ntotal_votes: {candidate_votes}\n-----------------------------------\n')
		winner = 0
		for line in candidate:
			index1 = candidate.index(line)
			
			if winner < candidate_votes[index1]:
				winner = candidate_votes[index1]
			print(f'{candidate[index1]} {percentvote[index1]} {candidate_votes[index1]}')
			textfile.write(f'{candidate[index1]} {percentvote[index1]} {candidate_votes[index1]}\n')
		index2 = candidate_votes.index(winner)
		textfile.write(f'-----------------------------------\nwinner {candidate[index2]}\n-----------------------------------')
		print(f'-----------------------------------\nwinner {candidate[index2]}\n-----------------------------------')
