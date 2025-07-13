coin = 50
cent = [5, 10, 25]
total_paid = 0

while coin > 0:
    print(f"Amount Due: {coin}")
    user = int(input("Insert Coin: ")) 
    if user in cent:
        coin = coin - user
        total_paid = total_paid + user

        if total_paid >= coin:
            print(f"Change Owed: {total_paid - 50}")