# Import necesary modules
import csv
import os

# Path to the dataset
file_path = 'Resources/election_data.csv'
analysis_dir = "Analysis"
analysis_file = os.path.join(analysis_dir, 'election_analysis.txt')

# Initialize variables
total_votes = 0
candidate_votes = {}

# Read the dataset
with open(file_path, 'r') as file:
    reader = csv.reader(file)
    header = next(reader)  # Skip the header row
    
    for row in reader:
        candidate = row[2]
        
        # Count the total number of votes
        total_votes += 1
        
        # Count the votes for each candidate
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1

# Calculate the percentage of votes each candidate won
candidate_percentages = {candidate: (votes / total_votes) * 100 for candidate, votes in candidate_votes.items()}

# Determine the winner of the election based on popular vote
winner = max(candidate_votes, key=candidate_votes.get)

# Prepare the analysis results
analysis_results = [
    "Election Results",
    "-------------------------",
    f"Total Votes: {total_votes}",
    "-------------------------"
]
for candidate, votes in candidate_votes.items():
    percentage = candidate_percentages[candidate]
    analysis_results.append(f"{candidate}: {percentage:.3f}% ({votes})")
analysis_results.append("-------------------------")
analysis_results.append(f"Winner: {winner}")
analysis_results.append("-------------------------")

# Write the analysis results to a text file
with open(analysis_file, 'w') as file:
    for line in analysis_results:
        file.write(line + "\n")

# Print the analysis results
for line in analysis_results:
    print(line)
