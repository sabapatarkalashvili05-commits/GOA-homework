# 1

list = [12, 34, 16, 6, 22, 33, 55, 77, 99]

positive = 0


for i in list:
    if i % 2 == 0:
        positive += i


print(positive)