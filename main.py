# 1

# list = [12,13,123,34,17,16,96]


# index = 0

# for i in list:
#     if index % 2 == 0:
#         print(i)
#     index += 1


numbers = [12, -123, 97, -64, -52, 72, 68, 0, 23, 0]

positive = 0
negative = 0

for i in numbers:
    if i > 0:
        positive += i
    elif i < 0:
        negative += 1
    else:
        print("zero")

print(positive)
print(negative)
