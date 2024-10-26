# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0

# Add more variables to track other necessary financial data
#Added more variables to track more financial data (profits and losses,
#months to track months, greatest increase and decrease, and to track previous month)
net_change_list = []
months = []
greatest_increase = ["", 0]
greatest_decrease = ["", 0]
previous_month_= 0

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    firstrow = next(reader)
    total_months = 1
    total_net =int(firstrow[1])
    previous_net = int(firstrow[1])

    for row in reader:
    
    # Track the total and net change
    #The += is another way of writing total months = total months + 1
        total_months += 1
        total_net += int(row[1])
        
        # Track the net change
        net_change = int(row[1]) - previous_net
        previous_net = int(row[1])
        net_change_list.append(net_change)
        months.append(row[0])
        
        # Calculate the greatest increase in profits (month and amount)
        if net_change > greatest_increase[1]:
            greatest_increase = [row[0], net_change]
        
        # Calculate the greatest decrease in losses (month and amount)
        if net_change < greatest_decrease[1]:
            greatest_decrease = [row[0], net_change]

# Calculate the average net change across the months
if len(net_change_list) > 0:
    average_change = sum(net_change_list) / len(net_change_list)
else:
    average_change = 0

# Generate the output summary
#Had to search how to make the output appear on multiple lines
#https://stackoverflow.com/questions/62372455/returning-output-in-multiple-lines
output = (
    "Financial Analysis\n" +
    "---------------------------\n" +
    "Total Months: " + str(total_months) + "\n" +
    "Total: $" + str(total_net) + "\n" +
    "Average Change: $" + str(round(average_change, 2)) + "\n" +
    "Greatest Increase in Profits: " + greatest_increase[0] + " ($" + str(greatest_increase[1]) + ")\n" +
    "Greatest Decrease in Profits: " + greatest_decrease[0] + " ($" + str(greatest_decrease[1]) + ")\n"
)

# Print the output

print(output)
# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)

