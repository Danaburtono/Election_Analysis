# Election_Analysis

## Overview of Election Audit:
A Colorado Board of Elections employee has provided me with the raw data for a recent election. I have been asked to perform an audit to evaluate the election results. I have done the following calculations- 
1. Calculate the total number of votes
2. Get a list of all the candidates that were voted for. 
3. Calculate the total number of votes for each candidate. 
4. Find the percentages for each candidate. 
5. Determine the winner of the election based on the popular vote.
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
By changing the geographic boundary, this script can be used for any election with simple modifications from counties to states or zip codes as long as the data is valid and void of errors the script will work correctly. Another use for this script could be to find the largest donated quantity to each campaign, by simply changing "candidates" to "donors", instead of ingesting "votes" it would ingest "dollars" also by changing the `increment =+ 1` to a `sum` we can determine the sum of donations for each candidate. 

![Screen Shot 2022-07-10 at 5 30 54 PM](https://user-images.githubusercontent.com/107026442/178168671-40269294-535f-4707-9cd6-b0a29cf0e2e4.png)

## Challenge Overview
 After finding all unique candidate names and counties it becames challenging to track variables as it gets ingested for computation. Some of the most challenging portions of this task was adjusting indentation to allow code to execute properly, understanding what should and should not lie within a for loop or if statement, and visualizing data as it gets ingested because we cannot physically see what is happening to the data we have to rely on our knowledge to visualize the state of the data as it undergoes processing. 

## Challenge Summary
Audit the election results and determine the winner of the election. Show the percentage and popular vote per candidate. Audit county votes and choose the county with the largest voter turnout. Show the percentage of voters and the quantity of votes per county.
