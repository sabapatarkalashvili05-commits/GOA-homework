# 1

# სიები (Lists) Python-ში არის მონაცემთა სტრუქტურა რომელიც გვაძლევს საშუალებას ერთ ცვლადში შევინახოთ რამდენიმე მნიშვნელობა.


#2

numbers = [1, 2, 3, 4, 5]

print(numbers[2])  


#3
numbers = [1, 3, 4, 6, 7, 9, 10, 12, 14, 15]

for num in numbers:
    if num % 3 == 0:
        print("divisible by 3")


#4

text = "programming"

print(text[-3:])


#5


names = ["Saba", "Nika", "Gio", "Tiko", "Ana"]

user_name = input("შეიყვანეთ თქვენი სახელი: ")

count = 0

for name in names:
    if name == user_name:
        print("user name")
        count += 1

print(count)

#6

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_sum = 0

for num in numbers:
    if num % 2 == 0:
        even_sum += num

print(even_sum)

#7

names = ["Saba", "Gio", "Nika", "Gvantsa", "Tiko"]

for name in names:
    if name.lower().startswith("g"):
        print(name, True)
