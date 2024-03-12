import pandas as pd
from pathlib import Path

# PyBank
# opening and setting up dataframe
csv = Path("PyBank/Resources/budget_data.csv")
df = pd.read_csv(csv)
header = df.head()
print(f'{header}\n')
# Count each month to determine total months
total_months = df['Date'].count()
# Sum balance sheet values to determine total balance at the end of the period
total_balance = df['Profit/Losses'].sum()
# Shift by 1 and subtract to determine monthly flow
df['avg_chg_bal'] = (df['Profit/Losses'] - df['Profit/Losses'].shift(1))
# Find average and reformat using mean Pandas mean and Py round function
avg_chg_bal = round(df['avg_chg_bal'].mean(), 2)
# Find max and reformat using mean Pandas mean and Py int function
max_total = int(df['avg_chg_bal'].max())
# Use loc function to find value that matches the greatest balance increase
max_month = df.loc[df['avg_chg_bal'] == max_total, :]
# Find min and reformat using min Pandas mean and Py int function
min_total = int(df['avg_chg_bal'].min())
# Use loc function to find value that matches the greatest balance decrease
min_month = df.loc[df['avg_chg_bal'] == min_total, :]
print(
    f'Financial Analysis:\n{total_months} Months in Total\nBalance of ${total_balance}\nAverage Balance of ${avg_chg_bal}\n'
    f'Largest Increase was ${max_total} in {max_month["Date"].values[0]}\nLargest Decrease was ${min_total} in {min_month["Date"].values[0]}\n')
PyBank = open("Stats/PyBank.txt", "w")
PyBank.write(
    f'Financial Analysis:\n{total_months} Months in Total\nBalance of ${total_balance}\nAverage Balance of ${avg_chg_bal}\n'
    f'Largest Increase was ${max_total} in {max_month["Date"].values[0]}\nLargest Decrease was ${min_total} in {min_month["Date"].values[0]}\n')
PyBank.close()
# PyPoll
# opening and setting up dataframe
csv = Path("PyPoll/Resources/election_data.csv")
df = pd.read_csv(csv)
header = df.head()
print(f'{header} \n')
total_votes = df['Ballot ID'].count()
# Using unique function to find each candidate used later in loc function
candidates = (df['Candidate'].unique())
print(f'candidate list: {candidates} \n')
# Using loc function to find each candidate's vote count
charles = df.loc[df['Candidate'] == 'Charles Casper Stockham', :]
charles_votes = charles['Ballot ID'].count()
diana = df.loc[df['Candidate'] == 'Diana DeGette', :]
diana_votes = diana['Ballot ID'].count()
rayman = df.loc[df['Candidate'] == 'Raymon Anthony Doane', :]
rayman_votes = rayman['Ballot ID'].count()
votes = [charles_votes, diana_votes, rayman_votes]
# Voting Stats for each candidate
print(f'Election Results:\n'
      f'{total_votes} Total Votes Cast \n'
      f'{charles_votes} Votes Cast for Charles Casper Stockham or {round(((charles_votes / total_votes) * 100), 2)}% of Votes Cast \n'
      f'{diana_votes} Votes Cast for Diana DeGette or {round(((diana_votes / total_votes) * 100), 2)}% of Votes Cast \n'
      f'{rayman_votes} Votes Cast for Raymon Anthony Doane or {round(((rayman_votes / total_votes) * 100), 2)}% of Votes Cast \n')
# Determine Winner
if max(votes) == charles_votes:
    print('Election Winner is Charles Casper Stockham!')
elif max(votes) == diana_votes:
    print('Election Winner is Diana DeGette!')
elif max(votes) == rayman_votes:
    print('Election Winner is Raymon Anthony Doane!')
# Create Txt with data
PyPoll = open("Stats/PyPoll.txt", "w")
PyPoll.write(f'Election Results:\n'
             f'{total_votes} Total Votes Cast \n'
             f'{charles_votes} Votes Cast for Charles Casper Stockham or {round(((charles_votes / total_votes) * 100), 2)}% of Votes Cast \n'
             f'{diana_votes} Votes Cast for Diana DeGette or {round(((diana_votes / total_votes) * 100), 2)}% of Votes Cast \n'
             f'{rayman_votes} Votes Cast for Raymon Anthony Doane or {round(((rayman_votes / total_votes) * 100), 2)}% of Votes Cast \n')
PyPoll.close()
