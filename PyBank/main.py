__author__ = 'nabbineni'

"""
Budget data Analysis:
- The total number of months included in the dataset
- The net total amount of "Profit/Losses" over the entire period
- The average of the changes in "Profit/Losses" over the entire period
- The greatest increase in profits (date and amount) over the entire period
- The greatest decrease in losses (date and amount) over the entire period

Assumptions:
The data is ordered by months in csv file and are in same order in the dictionary
There is only one row per month, unique months. No duplicates
"""

import os
import csv
from collections import OrderedDict

#read budget_data file
input_fil_path = os.path.join(".","Resources","budget_data.csv")

with open(input_fil_path, 'r') as csv_file:
    b_data = csv.reader(csv_file, delimiter = ',')
    next(b_data, None)

    #calculate total net profit/loss
    budget_data_dict = OrderedDict()
    total_net_amt = 0

    for b_row in b_data:
        budget_data_dict [b_row[0]] = int(b_row[1])
        total_net_amt = total_net_amt+int(b_row[1])

#calculate average of profit/loss change from month to month
items=list(budget_data_dict.items())
first_month = items[0]
last_month = items[len(budget_data_dict)-1]
avg_change = float((last_month[1] - first_month[1])) / (len(budget_data_dict)-1)

#calculate greatest profit increase and greatest profit decrease
profit_max = [("", 0, 0)]
loss_max = [("", 0 ,0)]

for i in range(len(items)-1):

    if (items[i+1][1]) -  (items [i][1]) > profit_max [0][2]:
        profit_max.pop()
        profit_max.append((items [i+1] [0], items [i+1] [1], (items[i+1][1]) -  (items [i][1])))

    if (items[i+1][1]) -  (items [i][1]) < loss_max [0][2]:
        loss_max.pop()
        loss_max.append((items [i+1] [0], items [i+1] [1], (items[i+1][1]) -  (items [i][1])))

#write results to output file
output_fil_path = os.path.join(".","Results","pyBank_output.txt")

with open(output_fil_path, "w") as text_file:
    text_file.write("Financial Analysis \n")
    text_file.write(25*"-")
    text_file.write("\nTotal Months: {}" .format(len(budget_data_dict)))
    text_file.write("\nTotal: ${}" .format(total_net_amt))
    text_file.write("\nAverage Change: $%.2f" % avg_change)
    text_file.write("\nGreatest Increase in Profits: {0}  $({1})".format(profit_max[0][0],profit_max[0][2]))
    text_file.write("\nGreatest Decrease in Profits: {0}  $({1})".format(loss_max[0][0],loss_max[0][2]))

#print results to the terminal
with open(output_fil_path, "r") as text_file:
    print(text_file.read())