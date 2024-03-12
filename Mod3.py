import pandas as pd
from pathlib import Path

# PyBank
csv = Path("PyBank/Resources/budget_data.csv")
df = pd.read_csv(csv)
header = df.head()
print(header)
total_months = df['Date'].count()
total_balance = df['Profit/Losses'].sum()
df['avg_chg_bal'] = (df['Profit/Losses'] - df['Profit/Losses'].shift(1))
avg_chg_bal = round(df['avg_chg_bal'].mean(), 2)
max_total = int(df['avg_chg_bal'].max())
max_month = df.loc[df['avg_chg_bal'] == 1862002, :]
min_total = int(df['avg_chg_bal'].min())
min_month = df.loc[df['avg_chg_bal'] == -1825558, :]
print(f'Financial Analysis:\n{total_months} Months in Total\nBalance of ${total_balance}\nAverage Balance of ${avg_chg_bal}\n'
      f'Largest Increase was ${max_total} in {max_month["Date"][79]}\nLargest Decrease was ${min_total} in {min_month["Date"][49]}\n')
#PyPoll
csv = Path("PyPoll/Resources/election_data.csv")
df = pd.read_csv(csv)
header = df.head()
print(header)
total_votes = df['Ballot ID'].count()
candidates = (df['Candidate'].unique())
print(f'candidate list: {candidates}')
charles = df.loc[df['Candidate'] == 'Charles Casper Stockham', :]
charles_votes = charles['Ballot ID'].count()
diana = df.loc[df['Candidate'] == 'Diana DeGette', :]
diana_votes = diana['Ballot ID'].count()
rayman = df.loc[df['Candidate'] == 'Raymon Anthony Doane', :]
rayman_votes = rayman['Ballot ID'].count()
votes = [charles_votes, diana_votes, rayman_votes]
print(f'Election Results:\n'
      f'{total_votes} Total Votes Cast \n'
      f'{charles_votes} Votes Cast for Charles or {round(((charles_votes / total_votes) *100), 2)}% \n'
      f'{diana_votes} Votes Cast for Diana or {round(((diana_votes / total_votes) * 100), 2)}% \n'
      f'{rayman_votes} Votes Cast for Rayman or {round(((rayman_votes / total_votes) * 100), 2)}% \n')
if max(votes) == charles_votes:
      print('Winner is Charles')
elif max(votes) == diana_votes:
      print('Winner is Diana')
elif max(votes) == diana_votes:
      print('Winner is Rayman')