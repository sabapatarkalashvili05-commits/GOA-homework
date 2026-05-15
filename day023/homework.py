#1

list = [12, 54, 3, 65, 55, 9]

list.pop()
list.append(21)

print(list)

#2

surname = input("Enter your surname: ")

print(surname[-6:] == "shvili")

#3

numbers = [1,2,3,4,5,6,7,8,9,10]

index = int(input("Enter index (1-5): "))

numbers.pop(index)       
numbers.insert(0, "change")  

print(numbers)

#4

asdasd = ["saba", "nika", "beka" , "giorgi", "luka" ]

for i in asdasd:
    print(i.upper)

#5

movie = input("Enter your favorite movie: ")
letter = input("Enter a letter: ")

print(movie.find(letter) != -1)
