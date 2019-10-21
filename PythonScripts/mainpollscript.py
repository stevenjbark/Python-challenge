import os
import csv

#Setup the file path for opening the election_test.csv file.
path = os.path.join('Resources', 'election_data.csv')

#Open the election_test.csv file using with statement
with open(path, 'r', newline='') as efile:

#Use csv to generate a reader object for analysis. Save header
    csvreader = csv.reader(efile, delimiter = ',')
    csv_header = next(csvreader)
    print(csv_header)
    
#As observed in the other PyBank file, the with option for opening files
#closes the file after use. Read the file contents into a list of lists for
#parsing and further data analysis.
    rawdata = []
    
    for line in csvreader:
        rawdata.append(line)
        
#To find the minimum number of unique candidates, we can use Python's Set
#class, which only allows for single membership in the set. Take the rawdata
#list, then extract a new list called candidates from the third position in
#the rawdata list.
candidates = []

for line in rawdata:
    candidates.append(line[2])
    
#Use the Set class to take the candidates list and convert to a unique Set list.
#Print the unique list for evaluation in the next steps.

unique = list(set(candidates))
print(unique)            
    
#There are 4 unique candidates ['Khan', 'Correy', 'Li', "O'Tooley"]. So now we
#need to count occurances for each candidate in the candidates list.
K = 0
C = 0
L = 0
O = 0

for name in candidates:
    if name == "Khan":
        K = K + 1
        
    if name == "Correy":
        C = C + 1
        
    if name == "Li":
        L = L + 1
    
    if name == "O'Tooley":
        O = O + 1
       
#Calculate total votes, the totals for each candidate, and the percentage for
#each candidate.
totalvotes = K + C + L + O

Khanpercent = round((K / totalvotes) * 100, 2)
Correypercent = round((C / totalvotes) * 100, 2)
Lipercent = round((L / totalvotes) * 100, 2)
OTooleypercent = round((O / totalvotes) * 100, 2)

#Comparison between the percentages of votes for each candidate.
winner = [Khanpercent, Correypercent, Lipercent, OTooleypercent]
winner.sort()

#Calculate final winner
final = []

if winner[3] == Khanpercent:
        final.append("Khan")
        final.append(Khanpercent)
    
elif winner[3] == Correypercent:
        final.append("Correy")
        final.append(Correypercent)
    
elif winner[3] == Lipercent:
        final.append("Li")
        final.append(Lipercent)
    
elif winner[3] == OTooleypercent: 
        final.append("O'Toole")
        final.append(OToolepercent)

#Print final results from data.
print("---------------------------------------------")        
print(f"Election Results Just In From All Precints with {totalvotes} Votes Cast!")
print("---------------------------------------------")       
print(f"Khan received {K} votes. This was {Khanpercent} percent of all votes cast.")
print(f"Correy received {C} votes.This was {Correypercent} percent of all votes cast.")
print(f"Li received {L} votes.This was {Lipercent} percent of all votes cast.")
print(f"O'Tooley received {O} votes. This was {OTooleypercent} percent of all votes cast.")
print("---------------------------------------------")
print(f"The Official-elect: {final[0]} with {final[1]} percent of the vote.")
        
#Setup and print file with these data using csvwriter object.
with open('ElectionResults.csv', 'w', newline='') as ER:  
    csvwriter = csv.writer(ER, delimiter = ',')
    csvwriter.writerow([1, (f"Election Results Just In From All Precints with {totalvotes} Votes Cast!")])
    csvwriter.writerow([2, ("---------------------------------------------")])
    csvwriter.writerow([3, (f"Khan received {K} votes. This was {Khanpercent} percent of all votes cast.")])
    csvwriter.writerow([4, (f"Correy received {C} votes.This was {Correypercent} percent of all votes cast.")])
    csvwriter.writerow([5, (f"Li received {L} votes.This was {Lipercent} percent of all votes cast.")])
    csvwriter.writerow([6, (f"O'Tooley received {O} votes. This was {OTooleypercent} percent of all votes cast.")])
    csvwriter.writerow([7, ("---------------------------------------------")])
    csvwriter.writerow([8, (f"The Official-elect: {final[0]} with {final[1]} percent of the vote.")])
    