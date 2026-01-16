#1
name = input("please enter your name:   ")

if name == "saba":
    print("hello")
else:
    print("bye")

#2
my_number = 24

user_number = int(input("enter your favourite number: "))

if user_number == my_number:
    print("Perfect")
elif user_number > my_number:
    print("More")
else:
    print("Less")

#3

my_name = "Saba"
my_age = 13

user_name = input("enter your name: ")
user_age = int(input("enter your age: "))

if user_name == my_name and user_age == my_age:
    print("Twins")
else:
    print("Not Twins")

#4

number = int(input("Enter a number: "))

if number % 3 == 0 and number % 5 == 0:
    print("The number is divisible by both 3 and 5")
else:
    print("The number is not divisible by both 3 and 5")


#5

password = input("Enter your password: ")

if len(password) < 8:
    print("Weak password")
else:
    print("Good password")




