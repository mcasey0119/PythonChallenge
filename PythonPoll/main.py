import os
import csv

#define path from which the file is
csvpath = os.path.join('Resources', 'election_data.csv')

#define variables
total_votes = 0
votes_for_khan = 0
votes_for_li = 0
votes_for_correy = 0
votes_for_otool = 0
#the order of candidates: Li, Correy, Khan, O'Tooley
candidate_votes = [0,0,0,0]

with open(csvpath) as csvfile:
    electiondata = csv.reader(csvfile)
    header = next(electiondata)

    for row in electiondata:
            total_votes = total_votes + 1

            if row[2] == "Li":
                votes_for_li = votes_for_li + 1
                candidate_votes [0] += 1
            elif row [2] == "Correy":
                votes_for_correy = votes_for_correy + 1
                candidate_votes [1] += 1
            elif row[2] == "Khan":
                votes_for_khan = votes_for_khan + 1
                candidate_votes [2] += 1
            elif row [2] == "O'Tooley":
                votes_for_otool = votes_for_otool + 1
                candidate_votes [3] += 1

    highest_votes = max(candidate_votes)
    winner_index = candidate_votes.index(highest_votes)

    winner = ""
    
    if winner_index == 0:
        winner = "Li"
    elif winner_index == 1:
        winner = "Correy"
    elif winner_index == 2:
        winner = "Khan"
    elif winner_index == 3:
        winner = "O'Tooley"

    print("Election Data")
    print("---------------")
    print(f"Total Votes: {total_votes}")
    print("---------------")
    print(f"Li: {candidate_votes[0]}, {round(votes_for_li/total_votes*100,3)}%")
    print(f"Correy: {votes_for_correy}, {round(votes_for_correy/total_votes*100,3)}%")
    print(f"Khan: {votes_for_khan}, {round(votes_for_khan/total_votes*100,3)}%")
    print(f"O'Tooley: {votes_for_otool}, {round(votes_for_otool/total_votes*100,3)}%")
    print("---------------")
    print(f"Winner: {winner}")

output = os.path.join('Analysis', 'election_data.txt')

with open(output, "w") as txt_file:
    txt_file.write("Election Data")
    txt_file.write("\n")
    txt_file.write("-----------------------")
    txt_file.write("\n")
    txt_file.write(f"Total Votes: {total_votes}")
    txt_file.write("\n")
    txt_file.write("---------------")
    txt_file.write("\n")
    txt_file.write(f"Li: {candidate_votes[0]}, {round(votes_for_li/total_votes*100,3)}%")
    txt_file.write("\n")
    txt_file.write(f"Correy: {votes_for_correy}, {round(votes_for_correy/total_votes*100,3)}%")
    txt_file.write("\n")
    txt_file.write(f"Khan: {votes_for_khan}, {round(votes_for_khan/total_votes*100,3)}%")
    txt_file.write("\n")
    txt_file.write(f"O'Tooley: {votes_for_otool}, {round(votes_for_otool/total_votes*100,3)}%")
    txt_file.write("\n")
    txt_file.write(f"Winner: {winner}")