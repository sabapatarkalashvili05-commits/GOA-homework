# 1

names = ["mariam", "lasha", "giorgi", "nino"]

if "giorgi" in names:
    names.remove("giorgi")

print(names)

# 2



my_list = ["mariam", "lasha", "giorgi", "nino"]


last_element = my_list.pop()


print("ბოლო ელემენტი ამოღებულია:", last_element)
print("მიღებული სია:", my_list)


# 3


names = ["mariam", "lasha", "giorgi", "nino"]


names.insert(2, "alexandre")


print(names)


# 4


names = ["lasha", "giorgi", "mariam"]
new_name = input("გთხოვთ, შეიყვანოთ თქვენი სახელი ინგლისურად: ")
names.append(new_name)
print(names)

# 5


numbers = [10, 20, 30, 40, 50]


favorite_number = int(input("შეიყვანე შენი საყვარელი რიცხვი: "))
index = int(input("შეიყვანე ინდექსი, სადაც უნდა ჩასვათ: "))


if 0 <= index < len(numbers):
    numbers.insert(index, favorite_number)
    print("განახლებული სია:", numbers)
else:
    print("Invalid index")

# 6

my_list = []

for _ in range(3):
    value = input("ჩაწერე ელემენტი სიაში: ")
    my_list.append(value)

print("მიღებული სია:", my_list)

# 7


names = ["mariam", "lasha", "giorgi", "nino"]


index = int(input("შეიყვანე ინდექსი, რომლის ელემენტსაც წაშლით: "))


if 0 <= index < len(names):
    names.pop(index)  
    print("განახლებული სია:", names)
else:
    print("Invalid index")