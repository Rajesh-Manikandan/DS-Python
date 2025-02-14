'''
Let us say your expense for every month are listed below,
January - 2200
February - 2350
March - 2600
April - 2130
May - 2190
Create a list to store these monthly expenses and using that find out,

1. In Feb, how many dollars you spent extra compare to January?
2. Find out your total expense in first quarter (first three months) of the year.
3. Find out if you spent exactly 2000 dollars in any month
4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
5. You returned an item that you bought in a month of April and
got a refund of 200$. Make a correction to your monthly expense list
based on this
'''

expenses = [2200, 2350, 2600, 2130,2190]

# 1. In Feb, how many dollars you spent extra compare to January?
print("In Feb, how many dollars you spent extra compare to January?")
print(expenses[1] - expenses[0]) # Complexity of this will be O(1)

# 2. Find out your total expense in first quarter (first three months) of the year.
print("Find out your total expense in first quarter (first three months) of the year.")
sum = 0
for expense in expenses[0:3]:
    sum = sum + expense
print(sum) # Time Complexity: O(3) → O(1) (since k is constant)

# 3. Find out if you spent exactly 2000 dollars in any month
print("Find out if you spent exactly 2000 dollars in any month")
print(2000 in expenses) # Complexity of this will be O(n)

# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
print("June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list")
expenses.append(1980) # Complexity of this will be O(n)


# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this
print('''
5. You returned an item that you bought in a month of April and
got a refund of 200$. Make a correction to your monthly expense list
based on this''')
expenses[3] = expenses[3] - 200 # Complexity of this will be O(1)