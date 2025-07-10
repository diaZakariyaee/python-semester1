from turtle import *

favouriteGames=str(input("Enter your 5 favourite games:"))
games=favouriteGames.split(",")
print (games)
userResponse=str(input('Do you like this game list or you want to change it?(Y/N)'))
while userResponse != "Y":
    favouriteGames=str(input("Enter your 5 favourite games:"))
    games=favouriteGames.split(",")
    print (games)
    userResponse=str(input('Do you like this game list or you want to change it?(Y/N)'))

if userResponse == "Y":
    print (games)
    print("great")
    done()


