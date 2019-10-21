#Import the os and csv modules for generating paths and processing the .csv file type.
import os
import csv

#Use the os.path.join to pass the "Resources" and "budget_data.csv" information to
#this os module. Generates a path to the .csv file from the Python-challenge directory
#and makes independent of OS as long as supported in Python. NOTE: This is relative
#path, not absolute path!
path = os.path.join("Resources", "budget_data.csv")

#Construct csv reader function for opening the budget_data.csv file.
with open(path, 'r', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    
#Read and store header row first and print the headers.
    csv_header = next(csvreader)
    print(csv_header)

#I think the csvreader is an object that closes after use, so read
#the remaining file rows into a list that can be used after the csvreader
#object is not accessible.
    banklist = []
    
    for row in csvreader:
       banklist.append(row)
       
#Process remaining information based on the created banklist.

#Total months is the number of rows in banklist.       
totalmonths = len(banklist)

#Summation of all of the bank profits/losses using a for loop. Set
#total = 0 to start, then each row has the total profits/losses in
#the second position of the row, or row[1]. Add up all row[1]. I used
#int(row[1]) in case the number was stored as a string.
total = 0
for row in banklist:
    total = total + int(row[1])
    
#Average is simply the total profits/losses divided by number of months.
average = total / totalmonths

#Average change would be for each month, how much did the profits/losses
#change in the next row. Will construct a new change list to store this
#information. Bank profits/losses from month(i) are subtracted from month(i+1)
#to calculate the difference. This is iterated down all of the months to 
#give a new list change. There will be 85 elements in this list where
#banklist has 86 (you can't calculate a difference on Month 1).
change = []

for i in range(len(banklist)-1):
    change.append(int(banklist[i+1][1]) - int(banklist[i][1]))
    
#Total for change is now the summation of all changes from month to month
#(totalchange) divided by the total number of months measured (len(change)).
#To get the appropriate decimal places, I used the round(number,2) function to
#round the average change in long form to 2 decimal places.
totalchange = 0

for row in change:
    totalchange = totalchange + row
    averagechange = round(totalchange/len(change), 2)
    
#Finding the minimum and maximum of a list simply uses the native min() and max() functions.
changemax = max(change)
changemin = min(change)

#The change list is correlated with the banklist, so the indexes can be correlated. 
#Index in Change List of 49 is the Index of 50 in BankList.
#Important to note the reference back to banklist:
#banklist[index for the row][first element in the row]
#index for row is the index for the changelist for the changemax or changemin elements
#and adding 1 to correlate properly.
for element in change:
    if element == changemax:
        increasemax = [(banklist[change.index(element)+1][0]), changemax]
        
    if element == changemin:
        decreasemin = [(banklist[change.index(element)+1][0]), changemin]


#Now print out all of the information requested in the proper formatting.
print("Financial Analysis")
print("-----------------------------------------------------------------------")
print(f"Total Months: {totalmonths}")
print(f"Total: ${total}")
print(f"Average Change: {averagechange}")
print(f"Greatest Increase in Profits: {increasemax[0]}, ${increasemax[1]}")
print(f"Greatest Decrease in Profits: {decreasemin[0]}, ${decreasemin[1]}")


#Use the with statement to open a new file with write privileges, then write
#the data from printing into the file.
with open("FinancialData.csv", 'w', newline='') as FD:
    csvwriter = csv.writer(FD, delimiter = ',')
    csvwriter.writerow([1, "Financial Analysis"])
    csvwriter.writerow([2, "-------------------------------------------------"])
    csvwriter.writerow([3, (f"Total Months: {totalmonths}")])
    csvwriter.writerow([4, (f"Total: ${total}")])
    csvwriter.writerow([5, (f"Average Change: {averagechange}")])
    csvwriter.writerow([6, (f"Greatest Increase in Profits: {increasemax[0]}, ${increasemax[1]}")])
    csvwriter.writerow([7, (f"Greatest Decrease in Profits: {decreasemin[0]}, ${decreasemin[1]}")])



