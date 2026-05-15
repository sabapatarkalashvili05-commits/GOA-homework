# 1
# slicing არის სიის ან სტრიქონის ნაწილის ამოღება start:end ფორმატით (slicing აბრუნებს რამდენიმე ელემენტს ერთად)
# indexing არის ერთი კონკრეტული ელემენტის ამოღება ინდექსით (indexing აბრუნებს ერთ ელემენტს)


# 2
numbers = [1, 2, 3, 4, 5, 6, 7]


print(numbers[4:])


# 3

name = input("შეიყვანე სახელი: ")
print(name[1:4])


# 4

my_surname = "Patarkalashvili" 
user_surname = input("enter your surname: ")

if user_surname[:5] == my_surname[:5]:
    print("almost same")
else:
    print("bye")


# 5

my_list = [1, 2, 3, 4, 5, 6, 7]

my_list[2] = "random"

print(my_list[:4])


# 6 ???





#7

surname = input("enter your surname: ")
choice = input("want to reverse your surname? (yes / no): ")

if choice == "yes":
    print(surname[::-1])
elif choice == "no":
    print(surname)
else:
    print("incorrect answer")
