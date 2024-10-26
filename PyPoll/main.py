# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
#I used relative paths to make easier to run 
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
#Storing candidate names and votes
candidate_options = []
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
#Started all variables with empty values until assigned later
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:
        
        # Increment the total vote count for each row
        total_votes += 1

        # Get the candidate's name from the row
        candidate_name = row[2]

        # If the candidate is not already in the candidate list, add them
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0

        # Add a vote to the candidate's count
        candidate_votes[candidate_name] += 1

# Open a text file to save the output
with open(file_to_output, "w") as txt_file:

    # Print the total vote count (to terminal)
    print("Election Results")
    print("----------------------------")
    print("Total Votes: " + str(total_votes))
    print("----------------------------")

    # Write the total vote count to the text file
    #Used this site: https://stackoverflow.com/questions/62372455/returning-output-in-multiple-lines
    txt_file.write("Election Results\n")
    txt_file.write("----------------------------\n")
    txt_file.write("Total Votes: " + str(total_votes) + "\n")
    txt_file.write("-----------------------------\n")

    # Loop through the candidates to determine vote percentages and identify the winner
    for candidate in candidate_votes:
        votes = candidate_votes[candidate]
        
        # Get the vote count and calculate the percentage
        vote_percentage = (votes / total_votes) * 100

        # Update the winning candidate if this one has more votes
        if votes > winning_count:
            winning_count = votes
            winning_candidate = candidate
            winning_percentage = vote_percentage


        # Print and save each candidate's vote count and percentage
        print(candidate + ": " + str(round(vote_percentage, 3)) + "% (" + str(votes) + ")")
        txt_file.write(candidate + ": " + str(round(vote_percentage, 3)) + "% (" + str(votes) + ")\n")

    # Generate and print the winning candidate summary
    print("-------------------------------")
    print("Winner: " + winning_candidate)
    print("-------------------------------")

    # Save the winning candidate summary to the text file
    txt_file.write("---------------------------\n")
    txt_file.write("Winner: " + winning_candidate + "\n")
    txt_file.write("---------------------------\n")

