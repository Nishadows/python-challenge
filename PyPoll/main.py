__author__ = 'nabbineni'

"""
PyPoll - Election Data Analysis:
- The total number of votes cast
- A complete list of candidates who received votes
- The percentage of votes each candidate won
- The total number of votes each candidate won
- The winner of the election based on popular vote.

Assumptions:
VoterIDs are unique, no duplicate voters
"""

import os
import csv

#read election_data file
input_fil_path = os.path.join(".","Resources","election_data.csv")

with open(input_fil_path, 'r') as csv_file:
    elect_data = csv.reader(csv_file, delimiter=',')
    next(elect_data, None)

    election_data_dict = {}
    total_votes = 0

    #calculate total votes and votes per candidate
    for e_row in elect_data:
        total_votes = total_votes + 1
        election_data_dict [e_row[2]] = election_data_dict.get(e_row[2],0)+1

#sort the keys in descending order of number of votes
sorted_election_data_dict = sorted(election_data_dict, key=election_data_dict.get, reverse=True)

#write results to output file
output_fil_path = os.path.join(".","Results","pyPoll_output.txt")

with open(output_fil_path, "w") as text_file:

    text_file.write("Election Results")
    text_file.write("\n"+25*"-")
    text_file.write("\nTotal votes: {0}".format(total_votes))
    text_file.write("\n"+25*"-")

    for e in sorted_election_data_dict:
        text_file.write("\n{0}: {1:.3f}% ({2})".format(e, round(((float(election_data_dict.get(e))/total_votes) * 100), 3), election_data_dict.get(e)))

    text_file.write("\n"+25*"-")
    text_file.write("\nWinner: {0}".format(list(sorted_election_data_dict)[0]))
    text_file.write("\n"+25*"-")

#print results to the terminal
with open(output_fil_path, "r") as text_file:
    print(text_file.read())