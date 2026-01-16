#1
#Conditional statements პიტონში გამოიყენება იმისთვის რომ კოდი შესრულდეს პირობის მიხედვით (True ან False)

#2
age = int(input("Enter age: "))

if age > 18:
    print("adult")
elif age > 13 and age < 18:
    print("teen")
else:
    print("child")

#3
name = input("Enter name: ")
age = int(input("Enter age: "))

if name == "giorgi":
    if age > 18:
        print("adult giorgi")
    else:
        print("not adult giorgi")
else:
    print("not giorgi")

#4

a = int(input("please enter first number: "))
b = int(input("please enter second number: "))

if a % b == 0:
    print("True")
else:
    print("False")


#5

name = input("Enter your name: ")
movie = input("Enter your favorite movie: ")

if name == "avto":
    print("you are avto")
elif name == "levani" and movie == "titanic":
    print("Levani loves titanic")
else:
    print("someone likes other film")






