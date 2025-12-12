'''
Write a Python program that can do the following:

- You have $50

- You buy an item that is $15, that has a 3% tax

- Using the print()  Print how much money you have left, after purchasing the item.
'''

my_money =  50
item_price = 15
tax_rate = .03

money_left = my_money - item_price - (item_price * tax_rate)

# numbers = input("2 con:")
# print(numbers)

days = int(input("How many days until your birthday? "))

print(round(days/7, 2))

# print(money_left)

# print(50 - 15 - (15 * .03))