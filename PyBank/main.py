# NAME
#    PyBank -- financial records analyzer
# 
# DESCRIPTION
#    Summarize financial records fetched from a CSV file.
# 
# AUTHOR
#    Gilberto Ramirez (gramirez77@gmail.com)
#    v1.0: June 2, 2019
# 
# REMARKS:
#    This is the third week homework for the UNC Data Analytics Boot Camp.

import os
import csv

# init summary variables
number_of_months = 0
total_profitloss = 0
average_change_amount = 0
average_change_months = 0
greatest_profits_increase_date = ''
greatest_profits_increase_amount = None
greatest_losses_decrease_date = ''
greatest_losses_decrease_amount = None

csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # discard the header
    next(csvreader)

    previous_profitloss = None
    for row in csvreader:
        number_of_months += 1
        total_profitloss += int(row[1])
        if previous_profitloss is not None:
            profitloss_delta = int(row[1]) - previous_profitloss
            average_change_amount += profitloss_delta
            average_change_months += 1
            if greatest_profits_increase_amount is None:
                greatest_profits_increase_amount = profitloss_delta
                greatest_losses_decrease_amount = profitloss_delta
            else:
                if profitloss_delta > greatest_profits_increase_amount:
                    greatest_profits_increase_date = row[0]
                    greatest_profits_increase_amount = profitloss_delta
                if profitloss_delta < greatest_losses_decrease_amount:
                    greatest_losses_decrease_date = row[0]
                    greatest_losses_decrease_amount = profitloss_delta
        previous_profitloss = int(row[1])

# create summary
summary = 'Financial Analysis\n'
summary += '----------------------------\n'
summary += f"Total Months: {number_of_months}\n"
summary += f"Total: ${total_profitloss}\n"
summary += f"Average Change: ${average_change_amount/(average_change_months):.2f}\n"
summary += f"Greatest Increase in Profits: {greatest_profits_increase_date} (${greatest_profits_increase_amount})\n"
summary += f"Greatest Decrease in Profits: {greatest_losses_decrease_date} (${greatest_losses_decrease_amount})\n"

# print summary to the terminal
print(summary, end='')

# export summary to a text file
with open('summary.txt', 'w', newline='') as txtfile:
    txtfile.write(summary)