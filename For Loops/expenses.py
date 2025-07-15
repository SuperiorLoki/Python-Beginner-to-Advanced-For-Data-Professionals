expenses = [1200, 1300, 1500, 1700]

total = 0
'''
for i in range(len(expenses)):
    total += expenses[i]
    
OR
'''

for expense in expenses:
    total += expense

print(total)


'''
for i in range(len(expenses)):
    print(f"On Month {i+1} of the year, the expense was ${expenses[i]}")

OR
'''
for i, expense in enumerate(expenses):
    print(f"On Month {i+1} of the year, the expense was ${expense}")


print(f"The total is {total}")

