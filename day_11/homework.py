#1
# or 
a = True or False        # True
b = False or False       # False
c = 5 > 3 or 2 > 10      # True
d = 10 == 5 or 4 != 3    # False

# and 
e = True and True        # True
f = True and False       # False
g = 7 > 3 and 2 < 5      # True
h = 10 > 20 and 5 == 5   # False

#2
name = input("შეიყვანე შენი სახელი: ")
age = int(input("შეიყვანე შენი ასაკი: "))
height = float(input("შეიყვანე შენი სიმაღლე (მეტრებში): "))

my_name = 'Saba'

if age > 18 and name == my_name and height > 1.80:
    print("პირობები დაკმაყოფილდა ")
else:
    print("პირობები არ დაკმაყოფილდა ")


#3
num1 = int(input("შეიყვანე პირველი რიცხვი: "))
num2 = int(input("შეიყვანე მეორე რიცხვი: "))

remainder = num1 % num2

print("ნაშთი არის:", remainder)


#4
age = int(input("შეიყვანე შენი ასაკი: "))

if age % 2 == 0:
    print("ასაკი ლუწია (ზუსტად იყოფა 2-ზე)")
else:
    print("ასაკი კენტია (ნაშთი არ არის ნული)")





