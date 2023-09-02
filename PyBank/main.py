#----------------------------------------------------------------------------------------------------------------------
# Analyze the records to calculate each of the following values:
# - Total number of months included in the dataset
# - Net total amount of "Profit/Losses" over the entire period
# - Changes in "Profit/Losses" over the entire period, and then the average of those changes
#   - changes_profits_losses = next_profits_losses - prev_profits_losses
#   - average_change = mean(changes_profits_losses excluding first month)
# - The greatest INCREASE in profits (date and amount) over the entire period
#   - greatest_increase = Max(changes_profits_losses)
# - The greatest DECREASE in profits (date and amount) over the entire period
#   - greatest_decrease = Min(changes_profits_losses)
#-----------------------------------------------------------------------------------------------------------------------

# Import modules needed to open, read, and write the dataset file
import os
import csv

# Definition for getting greatest increase or decrease
def get_greatest_value(iterable,is_increase = True):
    for i in iterable:
        if is_increase == True:
            if i[2] == max(c for d,p,c in iterable):
                greatest_value = i[0] + " ($" + str(i[2]) + ")"
        elif is_increase == False:
            if i[2] == min(c for d,p,c in iterable):
                greatest_value = i[0] + " ($" + str(i[2]) + ")"
    return greatest_value

# Set paths for input (budget_data.csv) and output (analysis.txt)
budget_csv = os.path.join("Resources","budget_data.csv")
output_file = os.path.join("analysis","analysis.txt")

# Set lists to store data
dates = []
profits_losses = []
differences = []

# Read the input csv file
with open(budget_csv, mode="r", encoding="UTF-8") as csvfile:

    # Split the data columns using ',' delimiter
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip the first row header since we don't need
    next(csvreader)

    # Loop through the recordset and assign values (cast int for profits/losses)
    for row in csvreader:
        dates.append(row[0])
        profits_losses.append(int(row[1]))

# Calculate the differences between two months
differences = [0 if i == 0 else (profits_losses[i] - profits_losses[i - 1]) for i,_ in enumerate(profits_losses)]

# Zip the dates, profits_losses, and new differences lists together as dict
new_zip = list(zip(dates,profits_losses,differences))

# Assign variables for analysis
total_number_months = len(dates)
total_amount = sum(i for i in profits_losses)
greatest_increase = get_greatest_value(new_zip)
greatest_decrease = get_greatest_value(new_zip,False)
average_change = round(sum(c for d,p,c in new_zip) / (total_number_months - 1),2)

# Build message output variable for printing and writing
msg_output = "-" * 50 + "\nFinancial Analysis\n" + "-" * 50
msg_output += "\nTotal Months: " + str(total_number_months) + "\nTotal: " + str(total_amount)
msg_output += "\nAverage Change: " + str(average_change) + "\nGreatest Increase in Profits: " + greatest_increase
msg_output += "\nGreatest Decrease in Profits: " + greatest_decrease

# Print the output
print(msg_output)

# Write the file
with open(output_file, "w", newline='') as datafile:    
    datafile.write(msg_output)