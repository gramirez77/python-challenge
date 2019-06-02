# NAME
#    PyPoll -- votes counter
# 
# DESCRIPTION
#    Votes counter based on records fetched from a CSV file.
# 
# AUTHOR
#    Gilberto Ramirez (gramirez77@gmail.com)
#    v1.0: June 2, 2019
# 
# REMARKS:
#    This is the third week homework for the UNC Data Analytics Boot Camp.

import os
import csv
import operator

# init election results variables
number_of_votes = 0
votes = {}

csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # discard the header
    next(csvreader)

    for row in csvreader:
        number_of_votes +=1
        votes[row[2]] = votes.get(row[2], 0) + 1

results = "Election Results\n"
results += "-------------------------\n"
results += f"Total Votes: {number_of_votes}\n"
results += "-------------------------\n"
for k, v in sorted(votes.items(), key=lambda item: item[1], reverse=True):
    results += f"{k}: {100*v/number_of_votes:.3f}% ({v})\n"
results += "-------------------------\n"
results += f"{max(votes.items(), key=operator.itemgetter(1))[0]}\n"
results += "-------------------------\n"

# print results to the terminal
print(results, end='')

# export results to a text file
with open('results.txt', 'w', newline='') as txtfile:
    txtfile.write(results)

