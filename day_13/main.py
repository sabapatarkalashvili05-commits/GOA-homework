#1

# for loop გამოიყენება მაშინ, როცა წინასწარ ვიცით 
# რამდენჯერ უნდა შესრულდეს ციკლი (მაგალითად range-ის გამოყენებით)

# while loop გამოიყენება მაშინ, როცა არ ვიცით ზუსტად
# რამდენჯერ შესრულდება ციკლი და ის გრძელდება
# მანამ, სანამ პირობა true (ჭეშმარიტი) იქნება


#2

for i in range(10, 39):
    print(i)


#3
i = 28

while i >= 2:
    print(i)
    i -= 2

#4

for i in range(101, 500, 2):
    print(i)


#5

name = "Saba"

for letter in name:
    print(letter)


#6

while i > 10:
    print("its less")
    i = i + 1

#ეს კოდი გამოიტანს errors რადგან ჩვენ არ ვიცით i ცვლადი რისი ტოლია



