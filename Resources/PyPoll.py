#The data we need to retrieve 
#The total number of votes cast 
#A complete list of candidated who recieved votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote

import csv
dir(csv)
#read files firect path and indirect path
#text file can be opened any any file editor
#binary file contains data that has not yet been converted to text.

#general format for opening a file 
#file_variable = open(filename, mode)
#file_variable: the name you assign the file to make it easier to reference in the script
#filename: a string specifying the name of the file
#mode: What you want to do with this file, read, write, creation, append, or reading and writing. 

#Assign variable for "Pathfile"
file_to_load = 'Resources/election_results.csv'
#Open the folder where it is located and read the file 
election_data = open(file_to_load, 'r')

#At the end of your analysis to close the file
election_data.close()

#using with and open syntax allows files to read and write files without open and close functions this ensures data isnt lost or corrupted
# Open the election results and read the file with OPEN & WITH statements
with open(file_to_load) as election_data:

     # To do: perform analysis.
     print(election_data)

#indirect path 
import os
dir(os)
file_to_load =os.path.join("Resources", "election_results.csv")
# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Print the file object.
     print(election_data)

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("Analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
open(file_to_save, "w")



# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Use the open statement to open the file as a text file.
outfile = open(file_to_save, "w")
# Write some data to the file.
outfile.write("Hello World")

# Close the file
outfile.close()



# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    txt_file.write("Arapahoe, Denver, Jefferson")


# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    txt_file.write("Counties in the Election\n")
    txt_file.write("-----------------------------------\n")
    txt_file.write("Arapahoe\nDenver\nJefferson")

#Start of official script
# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("/Users/danaburton/Desktop/DataClass/Election_Analysis/Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter, candidate options, and candidate votes.
total_votes = 0
Candidate_options = []
Candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row.
    headers = next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:
        # 2. Add to the total vote count.
        total_votes += 1

        #print the candidates name from each row
        Candidate_name = row[2]

        #Preform alternative to a unique function on candidate list, code will iterate over data and only list name if it appears atleast once. 
        if Candidate_name not in Candidate_options:
            Candidate_options.append(Candidate_name)
            #track each candidates votes
            Candidate_votes[Candidate_name] = 0
            
        #increment votes by 1 everytime the candidates name appears.
        Candidate_votes[Candidate_name] += 1
    #Determine percentages of votes per candidate
    for Candidate_name in Candidate_votes: 
        #Retrieve vote count of a candidate
        votes = Candidate_votes[Candidate_name]
        #Calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100
        #print the candidate name and percentage of votes
        #print(f"{Candidate_name}: received {vote_percentage:.1f}% of the vote.")
        print(f"{Candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Determine winning vote count and candidate
        # Determine if the votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent =
            # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # And, set the winning_candidate equal to the candidate's name.
            winning_candidate = Candidate_name

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
