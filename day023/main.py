# 1
# .upper() ყველა ასოს დიდად წერს 
# .lower() ყველა ასოს პატარა ასოდ წერს 
# .capitalize() პირველ ასოს დიდად წერს და დანარჩენს პატარა ასოდ

# 2

name = input("please enter your name: ")

print(name.upper())

# 3

strings = ["apple", "banana", "cherry", "date", "elderberry"]

for i in strings:  
    print(i.capitalize())

# 4
surname = input("please enter your surname: ")

t_in_surname = False

for i in surname:
    if i == "t":
        t_in_surname  = True

print(t_in_surname)


# 5

surname = input("please enter your surname: ")


case_type = input("how do you want your surnume to be written? (upper/lower/capitalize/none): ")


if case_type == "upper":
    print(surname.upper())
elif case_type == "lower":
    print(surname.lower())
elif case_type == "capitalize":
    print(surname.capitalize())
elif case_type == "none":
    print(surname)
else:
    print("incorrect input")



# 6


sentance = input("Enter a sentance: ")
symbol = input("Enter symbol: ")

print(sentance.find(symbol))

# 7


sentence = input("please enter a sentense: ")
symbol = input("please enter a symbol: ")

indexe = [] 
a = 0

for i in sentence:
    if i == symbol:
        indexe = indexe + [a] 
    a += 1

print(indexe)