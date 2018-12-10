#import the os module
import os
#import the csv module
import csv

budget_data_csv = os.path.join("Resource", "budget_data.csv")

#variable to hold total profits and losses
total = 0
#list to hold all csv data
BudgetInfo = []
#list to hold months column from csv data
Months = []
#list to hold profits and losses column from csv data
Amounts = []
#list of monthly amount changes
DifList = []

#open and read the csv file
with open(budget_data_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    header = next(csvreader)
    
    for row in csvreader:
#updating the total
       total += int(row[1])
#appending data to BudgetInfo list       
       BudgetInfo.append(row)
#appending data to Months list
       Months.append(row[0])
#appending data to Amounts list       
       Amounts.append(int(row[1]))
#finding the total months presented in the csv file        
TotalMonths = len(BudgetInfo)
#recording the total number of profits and losses
Period = len(BudgetInfo) - 1
#recording the amount from the first month in the csv file
FirstMonthTotal = BudgetInfo[0][1]
#finding the total for the last month of the csv file 
LastMonthTotal = Amounts[-1]
#finding average change for the year
AvgChange = (int(LastMonthTotal) - int(FirstMonthTotal)) / int(Period)
#populating the list of monthly amount changes
DifList = [y-x for x, y in zip(Amounts,Amounts[1:])]


#print results to terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {TotalMonths}")
print(f"Total: ${total}")
print("Average Change: $%.2f" %AvgChange)
print(f"Greatest Increase in Profits: {Months[(DifList.index(max(DifList)))+ 1]} (${max(DifList)})")
print(f"Greatest Decrease in Profits: {Months[(DifList.index(min(DifList)))+ 1]} (${min(DifList)})")

# Specify the file to write to
output_path = os.path.join("output", "PyBankCSV.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write data to csv file)

    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["----------------------------"])
    csvwriter.writerow([f"Total Months: {TotalMonths}"])
    csvwriter.writerow([f"Total: ${total}"])
    csvwriter.writerow(["Average Change: $%.2f" %AvgChange])
    csvwriter.writerow([f"Greatest Increase in Profits: {Months[(DifList.index(max(DifList)))+ 1]} (${max(DifList)})"])
    csvwriter.writerow([f"Greatest Decrease in Profits: {Months[(DifList.index(min(DifList)))+ 1]} (${min(DifList)})"]) 