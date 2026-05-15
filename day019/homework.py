#1

numbers = [3, 15, 8, 22, 10, 1, 19, 7, 10, 5]

for i in numbers:
    if i >= 10:
        print(i)


#2

name = input("Enter your name: ")


print("First letter:", name[0])
print("Last letter:", name[-1])

#3

numbers = [1, 2, 3, 4, 5]

reversed_numbers = numbers[::-1]

print(reversed_numbers)


#4


surname = input("Enter your surname: ")


reversed_part = surname[:5][::-1]


print("Reversed first 5 letters:", reversed_part)

#5

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


num = int(input("Enter a number between 1 and 5: "))


result = numbers[num -1::num]

print("Result:", result)
