#Importing the necessary modules/libraries
import os
import csv

# Path to collect data from the PyBank folder
budget_data = os.path.join('..', 'PyBank', 'budget_data.csv')

#Create our Counters
total_months = 0
total_pl = 0
value = 0
change = 0

#Create our Lists, to keep track of dates and profits 
dates = []
profits = []

#Opening and reading the CSV file
with open(budget_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    #Reading the header row
    csv_header = next(csvreader)

    #Creating variables to keep track of the changes between rows
    #Also reads the first row to test our changes
    first_row = next(csvreader)
    
    total_months += 1
    total_pl += int(first_row[1])
    value = int(first_row[1])
    
    #Going through each row of data after the header & first row 
    for row in csvreader:
        # Add the dates to our dates row defined above
        dates.append(row[0])
        
        # Calculate the change between dates, then add then add it to our
        # profits list defined above
        change = int(row[1])-value
        profits.append(change)
        value = int(row[1])
        
        #Add another value to our total months
        total_months += 1

        #Calculate our total net P/L over all the months 
        total_pl = total_pl + int(row[1])

    #Finds greatest increase in profits value 
    greatest_increase = max(profits)
    #Gets index for greatest increase in profits value 
    greatest_index = profits.index(greatest_increase)
    # Grabs the date corresponding with the index for the greatest increase in profits
    greatest_date = dates[greatest_index]

    #Finds greatest decrease in profits value, lowest increase 
    greatest_decrease = min(profits)
    #Gets index for lowest increase in profits value 
    worst_index = profits.index(greatest_decrease)
    # Grabs the date corresponding with the index for the lowest increase in profits
    worst_date = dates[worst_index]

    #Average change in "Profit/Losses between months over entire period"
    avg_change = sum(profits)/len(profits)
    

#Displaying information
print("Financial Analysis")
print("---------------------")
print(f"Total Months: {str(total_months)}")
print(f"Total: ${str(total_pl)}")
print(f"Average Change: ${str(round(avg_change,2))}")
print(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
print(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})")

# Exporting to .txt file
output = open("output.txt", "w")
line1 = "Financial Analysis"
line2 = "---------------------"
line3 = str(f"Total Months: {str(total_months)}")
line4 = str(f"Total: ${str(total_pl)}")
line5 = str(f"Average Change: ${str(round(avg_change,2))}")
line6 = str(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
line7 = str(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})")
output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7))

