things=[]

while True:
    thing=input("buy somethingthing:")
    if thing == "done":
        print(things + " 15$")
        break
    else:
        things.append(thing)