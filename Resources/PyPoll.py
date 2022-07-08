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

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("Analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    # Print each row in the CSV file.
    # for row in file_reader:
        #print(row)
        
    # Print the header row.
    headers = next(file_reader)
    print(headers)   