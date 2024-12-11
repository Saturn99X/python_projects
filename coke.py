coinvalues = [10, 25, 5]
amount_due = 50
while amount_due > 0:
    print(f"Amount Due: {amount_due}")
    insert_coin = int(input("insert coin: "))
    if insert_coin in coinvalues :
      amount_due = amount_due-insert_coin
    if amount_due <= 0:
        change_owed = abs(amount_due)
    else:
        continue

print(f"Change Owed: {change_owed}")
