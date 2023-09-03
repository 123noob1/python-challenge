# PyBank Challenge
- Please see <code>analysis.txt</code> under the analysis folder for the output from the <code>main.py</code>.
- <b>Approach methods to the problem:</b>
    1) Create a master list using zip for analysis for below lists:
        - Extract months and profits/losses into their own list.
        - Create a new list showing differences between current and previous month's profits/losses. First month is default to 0.
    2) Get total months by using len() function to determine the length of months list.
    3) Get net total by summing the list for profits/losses.
    4) Get average change by dividing the sum() of differences to the total number of months minus one.
    5) Greatest increase and decrease are calculated by using a defined def function <code>get_greatest_value(iterable,is_increase = True)</code>.
    6) Final output is stored in a msg_output variable for printing and writing.
- Refer to the <b>References</b> section for sources that were used to help in solving this challenge.

# PyPoll Challenge
- Please see <code>analysis.txt</code> under the analysis folder for the output from the <code>main.py</code>.
- <b>Approach methods to the problem:</b>
    1) Create a master list using zip for analysis for below list:
        - Extract ballot_ids, counties, and candidates into their own list.
    2) Create a dictionary for a complete list of unique candidates and counties they were in with the ballot counts.
    3) Get total number of votes by len() function of the master list.
    4) Defined a definition <code>get_candidate_stat(search_candidate, iterable)</code> to get total vote counts for the candidate.
        - Using this total vote counts, we can get the percentage by dividing the vote counts to the total number of votes overall.
    5) To determine the winner, conditional statements were used using the percent of votes from each candidate.
    6) Final output is stored in a msg_output variable for printing and writing.
- Refer to the <b>References</b> section for sources that were used to help in solving this challenge.
# References
- https://www.w3schools.com/python/python_lists_comprehension.asp - for comprehension examples
- https://www.learndatasci.com/solutions/python-list-comprehension/ - for comprehension explanation and examples
- https://www.youtube.com/watch?v=2KiPhpJ_JQE - explanation on nested dictionary data structure
- https://stackoverflow.com/questions/364621/how-to-get-items-position-in-a-list - for enumartion examples through a list