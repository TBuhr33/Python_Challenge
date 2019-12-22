#import the os and csv modules
import os
import csv

#declare the path for reading the file
BankCSV = os.path.join('PyBank_CSV.csv')
OutputBankCSV = os.path.join('OutputPyBank.txt')

#setup the outline for the print
print("Financial Analysis")
print("----------------------------------------")

#find total months by counting rows in csv
with open(BankCSV, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    #sum of rows code taken from stackoverflow forum
    months = sum(1 for row in csvreader)
    print(f"Total Months:  {str(months)}")

#get the sum of the 2nd column [1]
with open(BankCSV, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    header = next(csvreader)
    netMoney = sum(float(row[1]) for row in csvreader)
    print(f"Total: ${netMoney}")

#find the average of the 2nd column [1]
#ask in office hours how this is supposed to be done??
AverageChange = float(round(netMoney/months,2))
print(f"Average Change: ${AverageChange}")

#find greatest increase profit
with open(BankCSV, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    header = next(csvreader)
    #figure out how to use relative, without multiple print statements
    #wanna be universal, not just using reference
    maxVal = 1100000   
    
    for row in csvreader:
        if float(row[1]) > float(maxVal):
            maxVal = row[1]
            print(f"Greatest Increase in Profits: {row[0]} (${maxVal})")

#find greatest decrease
with open(BankCSV, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    header = next(csvreader)
    #again, ask about the multiple print statements
    minVal = -1100000  
    
    for row in csvreader:
        if float(row[1]) < float(minVal):
            minVal = row[1]
            print(f"Greatest Decrease in Profits: {row[0]} (${minVal})")


##after struggling with this for a long time, realized i should have 
##established variables in the beginning, and could have only opened
##and used the pathway once, reducing the total code and making it much 
##cleaner and easier to understand.   Also would have solved some of the 
##troubleshooting such as finding the max/min values.  

##make note to utilize variables for 2nd part/pypoll

#export to text
with open (OutputBankCSV, 'w', newline='') as textfile:
    print(" Financial Analysis", file=textfile)
    print("----------------------------------", file=textfile)
    print(f"Total Months:  {str(months)}",  file=textfile)
    print(f"Total: ${netMoney}", file=textfile)
    print(f"Average Change: ${AverageChange}", file=textfile)
    print(f"Greatest Increase in Profits: {row[0]} (${maxVal})", file=textfile)
    print(f"Greatest Decrease in Profits: {row[0]} (${minVal})", file=textfile)