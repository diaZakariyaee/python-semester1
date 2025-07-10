game = 'mindcraft' # string
food= 'pizza'
#print("My favorite game is " , game)
#print("My favorite game is " , game+"!")
print("My favorite game is for", "{game}!") # f string  
print("My favorite food is for", "{food}!") # f string
#-----------------------------------------------------
text ="arsham Diana Dia Dilan Radvin"
new = text.split("")
print(new)
#-----------------------------------------------------
text2="apple"
new2 = text2.split(" ")
print(new2)
#-----------------------------------------------------
# name = input("name:  ").capitalize() # ===> DIA => dia
#name = input("name:  ").upper() # ===> dia => DIA
name = input("name:  ").upper() # ===> diana => Diana 
print(name) 
#-----------------------------------------------------
text3 = "arsham Diana Dia Dilan Radvin"
print(text3.title())   