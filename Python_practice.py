from calendar import c
from itertools import count


counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])
#The if-else statement is also referred to as a dual-alternative decision statement. An if-else statement will execute one block of statements, or path, if a condition is true, or another block of statements if the condition is false
temperature = int(input("What is the temperature outside?"))
if temperature > 80:
    print("Turn on the AC please")
else: 
    print("Its nice in here, please dont turn on the AC.")
#nested if-else statements need to have exactly correct indentation
score = int(input("What did you score on the test?"))
if score >= 90:
    print('You got an A!')
else:
    if score >= 80:
        print('You got a B!')
    else:
        if score >= 70:
            print('You got a C.')
        else:
            if score >= 60:
                print('You got a D.')
            else:
                print('You straight up failed.')
#if-elif-else dont need indentation 
score = int(input("What is your test score? "))

# Determine the grade.
if score >= 90:
    print('Your grade is an A.')
elif score >= 80:
    print('Your grade is a B.')
elif score >= 70:
    print('Your grade is a C.')
elif score >= 60:
    print('Your grade is a D.')
else:
    print('Your grade is an F.')

#The length of the decision structure determines whether you use a nested if-else statement or the if-elif-else statement. If you have to scroll horizontally on your computer screen to see all the code in an if-else statement , then you should use an if-elif-else statement.

#In Operator: Returns true if a sequence with the specified value is present in the object
counties = ["Arapahoe","Denver","Jefferson"] 
if "Arapahoe" in counties: 
    print("True")
else: print("False")
#No In Operator: Returns true if a sequence with the specifed value is not present in the object
counties = ["Arapahoe","Denver","Jefferson"] 
if "El Paso" not in counties: 
    print("True") 
else: print("False")

if "El Paso" in counties:
    print("El Paso is part of the list")
else: print("El Paso is not part of the list")

#And: All conditions need to be met to have a True statement
x = 5 
y = 5
if x == 5 and y == 9:
    print("True") 
else: 
    print("False")
#Or: Only one condition needs to be met to have a true statement
x = 5 
y = 5
if x == 3 or y == 5:
    print("True")
else: 
    print("False")
#Not: Evaulates a boolean expression. The expresion is true if the conditional is false
x = 5 
y = 5
#this statmet is true because x is not greater that y, if x=6 then the statement would be false.
if not(x > y):
    print("True") 
else: 
    print("False")
#In & And Statements
counties
if "Arapahoe" in counties and "El Paso" in counties:
    print("Both counties are on the list")
else:
    print("One or more counties are missing from the list")
#In & Or Statements 
if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list.")
else:
    print("Arapahow and El Paso are not in the list")

#Loops
# There are two repetition structures: condition- controlled Loop and count controled loop. 
# Condition-control loop uses true or false statements this is also called while loops.
# Count Controlled loop: repeats a specific number of times depending on the conditions this is called a For loop. 

for county in counties: 
    print(county)
county
#Range simplifies the process of writing a for loop by creatiing an iterable object or list.
numbers = [0,1,2,3,4,5]
for num in numbers: 
    print(num)
for num in range(5):
    print(num)
#indexing 
#if a list contains strings, we'll need to get the length of the list as an integer for the range().
for i in range(len(counties)):
    print(counties[i])
range(len(counties))
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county in counties_dict:
    print(county)
for county in counties_dict.keys():
    print(county)
for voters in counties_dict.values():
    print(voters)
for county in counties_dict:
    print(counties_dict[county])
for county in counties_dict:
    print(counties_dict.get(county))
for county, voters in counties_dict.items():
    print (county "county has" voters "registered voters.")
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]  
for county_dict in voting_data:
    print(county_dict)
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]
for county_dict in voting_data:
    print(county_dict)
for i in range(len(voting_data)):
    print(voting_data[i]["county"])
for county in counties_dict.keys():
    print(county)
#Nested Loop 
for county_dict in voting_data: 
    print(county_dict.values())
for county_dict in voting_data:
     print(county_dict['registered_voters'])

