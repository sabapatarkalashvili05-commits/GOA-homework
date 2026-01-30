#1
numbers = [3, 7, 12, 5, 20, 10, 15]

for num in numbers:
    if num > 10:
        print(num)

#2
items = [10, 3.14, "hello", True, [1, 2], (3, 4) ]

for item in items:
    print(type(item))

#3
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sum = 0
for num in numbers:
    sum += num

print(sum)

#4
items = ["apple", "banana", "cherry", "orange"]

index = 0
for item in items:
    print(index, item)
    index += 1

#5
list = [10, 20, 30, 40, 50, 60]

index = 0
for item in list:
    if index % 2 == 0:
        print(item)
    index += 1

#6

numbers = [3, -1, 0, 7, -5, 0, 2, -8]

positive = 0
negative = 0
zero_count = 0


for num in numbers:
    if num > 0:
        positive += num       
    elif num < 0:
        negative += 1         
    else:
        zero_count += 1       


print("Positive sum:", positive)
print("Negative count:", negative)
for i in range(zero_count):
    print("zero")




