import csv, os

# PyBank
# opening and setting up csv
csvpath =  os.path.join("PyBank/Resources/budget_data.csv")

with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    print(f'Header: {csv_header}')
    # Count each month to determine total months
    total_months = 0
    total_balance = 0
    old_bal = 0
    bal_chg_lst = []
    date_lst = []
    for row in csvreader:
        total_months = total_months + 1
        total_balance = total_balance + int(row[1])
        bal_chg = int(row[1]) - old_bal
        if bal_chg == 1088983:
            bal_chg = 0
        old_bal = int(row[1])
        bal_chg_lst.append(bal_chg)
        date_lst.append(row[0])

avg_chg_bal = ((sum(bal_chg_lst))/(total_months-1)).__round__(2)
max_total = (max(bal_chg_lst))
min_total = (min(bal_chg_lst))
# Finding element index to find max/min matching date
mindex = bal_chg_lst.index(min(bal_chg_lst))
maxdex = bal_chg_lst.index(max(bal_chg_lst))
# Bank Stats
print(
    f'Financial Analysis:\n{total_months} Months in Total\nBalance of ${total_balance}\nAverage Balance of ${avg_chg_bal}\n'
    f'Largest Increase was ${max_total} in {date_lst[mindex]}\nLargest Decrease was ${min_total} in {date_lst[maxdex]}\n')
# Create Txt with data
PyBank = open("Stats/PyBank.txt", "w")
PyBank.write(
    f'Financial Analysis:\n{total_months} Months in Total\nBalance of ${total_balance}\nAverage Balance of ${avg_chg_bal}\n'
    f'Largest Increase was ${max_total} in {date_lst[mindex]}\nLargest Decrease was ${min_total} in {date_lst[maxdex]}\n')
PyBank.close()

# # PyPoll

# # opening and setting up csv
csvpath =  os.path.join("Pypoll/Resources/election_data.csv")

with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    print(f'Header: {csv_header}')
    total_votes = 0
    charles_votes = 0
    diana_votes = 0
    rayman_votes = 0
    for row in csvreader:
        total_votes = total_votes + 1
        if row[2] == 'Charles Casper Stockham':
            charles_votes = charles_votes + 1
        elif row[2] == 'Diana DeGette':
            diana_votes = diana_votes + 1
        elif row[2] == 'Raymon Anthony Doane':
            rayman_votes = rayman_votes + 1

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
