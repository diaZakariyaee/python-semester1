games=[]

while True:
    game=input("enter a game:")
    if game == "end":
        print(games)
        break
    else:
        games.append(game)