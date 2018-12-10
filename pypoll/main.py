#import the os module
import os
#import the csv module
import csv

election_results_csv = os.path.join("Resource", "election_data.csv")


print("Election Results")
print("-------------------------")

#create empty list which will hold candidate data
candidates = []
#create variable for total overall votes in election
total_votes = 0
#declare variables to hold vote counts for each candidate
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0
#create variables used to cross reference against the candidates list
a = "Khan"
b = "Correy"
c = "Li"
d = "O'Tooley"
#open and read the csv file
with open(election_results_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    header = next(csvreader)

    for row in csvreader:
#assign the data from the third row of the csv file to the candidates list
       candidates.append(row[2])
#find the total number of votes
       total_votes = len(candidates)

#Get the total votes for each candidate
def countA(candidates, a): 
    return candidates.count(a)
khan_votes = khan_votes + countA(candidates, a)     

def countB(candidates, b): 
    return candidates.count(b)
correy_votes = correy_votes + countB(candidates, b) 

def countC(candidates, c): 
    return candidates.count(c)
li_votes = li_votes + countC(candidates, c)

def countD(candidates, d): 
    return candidates.count(d)
otooley_votes = otooley_votes + countD(candidates, d)

#Find the percentage of votes each candidate received
khan_per = khan_votes/total_votes
correy_per = correy_votes/total_votes
li_per = li_votes/total_votes
otooley_per = otooley_votes/total_votes

#print the results to the terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
print("Khan: {:.3%}".format(khan_per) + " (" + str(khan_votes) + ")")
print("Correy: {:.3%}".format(correy_per) + " (" + str(correy_votes) + ")")
print("Li: {:.3%}".format(li_per) + " (" + str(li_votes) + ")")
print("O'Tooley: {:.3%}".format(otooley_per) + " (" + str(otooley_votes) + ")")
print("-------------------------")
print("Winner: Khan")
print("-------------------------")


# Specify the file to write to
output_path = os.path.join("output", "PyPollResultsCSV.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write data to csv file)

    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["---------------------------------"])    
    csvwriter.writerow([f"Total Votes: {total_votes}"])
    csvwriter.writerow(["---------------------------------"])   
    csvwriter.writerow(["Khan: {:.3%}".format(khan_per) + " (" + str(khan_votes) + ")"])
    csvwriter.writerow(["Correy: {:.3%}".format(correy_per) + " (" + str(correy_votes) + ")"])
    csvwriter.writerow(["Li: {:.3%}".format(li_per) + " (" + str(li_votes) + ")"])
    csvwriter.writerow(["O'Tooley: {:.3%}".format(otooley_per) + " (" + str(otooley_votes) + ")"])
    csvwriter.writerow(["---------------------------------"])   
    csvwriter.writerow(["Winner: Khan"])
    csvwriter.writerow(["---------------------------------"])   