import os
import csv

# Path to collect data from the Resources folder
budget_csv = os.path.join('..', 'PyBank', 'budget_data.csv')

# Define the function and have it accept the 'budget data' as its sole parameter
def financial_analysis(budget_data):
    
    date = str(budget_data[0])
    PandL = int(budget_data[1])

    # Total number of months can be found by counting the dates 
    Total_Months = len(date)

    #Net amount of profit/losses can be found by summing the profit losses 
    Total = sum(PandL)

    #Average of the change in P/L can be found by averaging the column 
    #Av_Change = (Total/Total_Months)

    # Calculate greatest increase in profits 
    #if loss_percent > 50:
    #    type_of_wrestler = "Jobber"
    #else:
    #    type_of_wrestler = "Superstar"

    # Print out the wrestler's name and their percentage stats
    print("Financial Analysis")
    print("---------------------------------------------------")
    print(f"Total Months: {Total_Months}")
    print(f"Total: {str(Total)}")
    #print(f"Average Change: {str(Av_Change)}")
    #print(f"DRAW PERCENT: {str(draw_percent)}")
    #print(f"{name} is a {type_of_wrestler}")
# Read in the CSV file
with open(budget_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    # Print Function 
    financial_analysis
