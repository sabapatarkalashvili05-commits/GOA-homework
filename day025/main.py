# 1

# ფუნქცია არის კოდის ბლოკი რომელსაც სახელი აქვს და რომელიც ასრულებს კონკრეტულ
# ამოცანას/დავალებას ის საშუალებას გაძლევს ერთი და იგივე კოდი ბევრჯერ გამოიყენო

# 2


def sum_of_3(x, g, z):
    total = x + g + z
    return total

print(sum_of_3(3, 67, 4))


# 3


def list_length(list):
    return len(list)


print(list_length([1, 3, 4, 5]))

# 4

def average(nums):
    return sum(nums) / len(nums)

print(average([1, 2, 3]))

# 5

list = ["amiko", "saba", "gio", "adriana", "luka"]

def insert_string(s, index):
    list.insert(index, s)
    return list

user_string = input("enter any string:3: ")
user_index = int(input("enter ant index:3: "))

print(insert_string(user_string, user_index))

# 6
def my_len(lst):
    count = 0

    for _ in lst:
        count += 1
    return count

numbers = [10, 20, 30, 40]
print(my_len(numbers))  

text = "Python"
print(my_len(text))     

# 7 ????
