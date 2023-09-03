#----------------------------------------------------------------------------------------------------------------------
# Analyze the records to calculate each of the following values:
# - Total number of votes cast
#   - total_number = len(rows - 1)
# - Complete list of candidates who received votes
#   - unique_candidates
# - Percentage of votes each candidate won
#   - percent_won_candidate = sum(candidate_votes) / total_number
# - Total number of votes each candidate won
#   - total_votes_pcandidate = count(unique_candidate)
# - Winner of the election based on popular vote
#   - winner = highest percent votes yield by candidate
#-----------------------------------------------------------------------------------------------------------------------

# Import modules needed to open, read, and write the dataset file
import os
import csv

# Define function to be called to return a candidate stat 
# (total vote/candidate and percent overall from total number of voters)
def get_candidate_stat(search_candidate, iterable):
    candidate_total_vote = 0

    if search_candidate in iterable:
        candidate_total_vote = sum([value for value in iterable[search_candidate].values()])

    return candidate_total_vote

# Set paths for input (election_data.csv) and output (analysis.txt)
election_csv = os.path.join("Resources","election_data.csv")
output_file = os.path.join("analysis","analysis.txt")

# Set lists to store data
ballot_ids = []
counties = []
candidates = []
election_list = []

# Read the input csv file
with open(election_csv, mode="r", encoding="UTF-8") as csvfile:

    # Split the data columns using "," delmiter
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header row
    header = next(csvreader)

    # Store the columns into respective list variables
    for row in csvreader:
        ballot_ids.append(row[0])
        counties.append(row[1])
        candidates.append(row[2])

# Zip the 3 lists into one
election_list = list(zip(ballot_ids,counties,candidates))
election_stat = {}

# Get unique lists of candidates and counties then populate a dictionary containing unique candidates as key with subdictionary 
# for counties with total count of vote for each county that each candidate was in
unique_candidates = set(candidates)
unique_counties = set(counties)

for candidate in unique_candidates:
    election_stat[candidate] = {}

    for county in unique_counties:
        election_stat[candidate][county] = len([ballot_id for ballot_id,county_,candidate_ in election_list if candidate == candidate_ and county == county_])
        
# Calculate values and assign to appropriate variables for analysis
total_number = len(election_list)

stockham_total = get_candidate_stat("Charles Casper Stockham",election_stat)
stockham_percent = round((stockham_total / total_number) * 100,3)

degette_total = get_candidate_stat("Diana DeGette",election_stat)
degette_percent = round((degette_total / total_number) * 100, 3)

doane_total = get_candidate_stat("Raymon Anthony Doane",election_stat)
doane_percent = round((doane_total / total_number) * 100, 3)

# Determine the winner based on the percentage using if, elif, and else conditions
if stockham_percent > (degette_percent + doane_percent):
    winner = "Charles Casper Stockham"
elif degette_percent > (stockham_percent + doane_percent):
    winner = "Diana DeGette"
else:
    winner = "Raymon Anthony Doane"

# Build message for output to terminal and text file
msg_output = "Election Results\n" + ("-" * 50)
msg_output += "\nTotal Votes: " + str(total_number) + "\n" + ("-" * 50)
msg_output += "\nCharles Casper Stockham: " + str(stockham_percent) + "% (" + str(stockham_total) + ")"
msg_output += "\nDiana DeGette: " + str(degette_percent) + "% (" + str(degette_total) + ")"
msg_output += "\nRaymon Anthony Doane: " + str(doane_percent) + "% (" + str(doane_total) + ")\n" + ("-" * 50)
msg_output += "\nWinner: " + winner + "\n" + ("-" * 50)

# Print out to the terminal
print(msg_output)

# Write the msg_output to the text file defined from the earlier set paths
with open(output_file, "w", newline="") as datafile:
    datafile.write(msg_output)