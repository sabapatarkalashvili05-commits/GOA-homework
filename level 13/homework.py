#1

for i in range(0, 51):
    if i % 2 != 0:
        print(i)

#2

surname = input("შეიყვანეთ თქვენი გვარი: ")

for letter in surname:
    print(letter)

#3

for i in range(150):
    if i % 2 == 0:
        print("even")
    else:
        print("odd")


#4

for i in range(20, -1, -1):
    print(i)


#5

original_password = "mypassword123"

user_password = ""

while user_password != original_password:
    user_password = input("enter password: ")

print("password correct acces granted!")

