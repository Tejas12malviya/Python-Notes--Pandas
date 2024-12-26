# Write a Python program that can do the following:

# - You have $50

# - You buy an item that is $15, that has a 3% tax

# - Using the print()  Print how much money you have left, after purchasing the item.

money_got=50
item_cost=15
tax=0.03
item_price=item_cost+item_cost*tax

print(f"item_price : {item_price}")
print(f"money_left : {money_got-item_price}")


"""
String Assignment. (This can be tricky so feel free to watch solution so we can do it together)

- Ask the user how many days until their birthday

- Using the print()function. Print an approx. number of weeks until their birthday

- 1 week is = to 7 days.

"""

Remaining_days=int(input("How many days until your birthday? "))
weeks=Remaining_days//7
days=Remaining_days%7

print(f" {weeks} weeks and {days} days until your birthday")
