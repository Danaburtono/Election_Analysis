# Election_Analysis

## Overview of Election Audit:
A Colorado Board of Elections employee has provided the raw data for the recent election, they ask me to preform an audit to evaulate the results of the election. I have been asked to-
1. Calculate total number of votes
2. Get a list of all the candidates that where voted for. 
3. Calculate the total number votes for each canduidate. 
4. Find the percentages for each candidate. 
5. Determine the winner of the election based on populat vote.
6. Determine the contributing counties
7. Calculate the total number of votes for each county
8. Find a percentage of votes per county
9. Determine the largest voter turnout

## Election Audit Results: 
- There were a total of 369,711 total votes.
-Counties:
    - Jefferson: 10.5% (38,855)
    - Denver: 82.8% (306,055)
    - Arapahoe: 6.7% (24,801)
    - Denver had the largest amount of votes.
-Candidates:
    - Charles Casper Stockham: 23.0% (85,213)
    - Diana DeGette: 73.8% (272,892)
    - Raymon Anthony Doane: 3.1% (11,606)
Winner of Election:
    - Winner: Diana DeGette
    - Winning Vote Count: 272,892
    - Winning Percentage: 73.8%
    
![Screen Shot 2022-07-10 at 5 33 04 PM](https://user-images.githubusercontent.com/107026442/178168747-b8936c7b-24f6-4344-a7f5-2ab28b66d22a.png)

## Election-Audit Summary
This script can be used for any election with simple modifications from counties to want states or zipcodes as a geographic boundary to determine what areas contribute more to elections. As long as the data is valid and void of errors the script will work correctly. Another use for this script could be to find largest donated quantity to each campaigns, by simply changing "candidates" to "donors", instead of ingesting "votes" it would ingest "dollars" also by changing the `increment =+ 1` to a `sum` we can determine sum of donations for each candidate. 

![Screen Shot 2022-07-10 at 5 30 54 PM](https://user-images.githubusercontent.com/107026442/178168671-40269294-535f-4707-9cd6-b0a29cf0e2e4.png)

## Challenge Overview
 After finding all unique candidate names and counties it becomes chanllenging to tracking variables as it gets manipulated for computation. The some of the most challenging portion of this task was adjusting intendation to allow code to execute properly, understanding what should and should not lie within a for loop or if statement, and visualizing data as it gets manipulated because we cannot always physically see what is happening to the data we have to rely on our knowledge to visualize the state of the data as it undergoes processing. 

## Challenge Summary
Audit the election results and determine the winner of the election. Show the percentage and popular vote per candidate.
