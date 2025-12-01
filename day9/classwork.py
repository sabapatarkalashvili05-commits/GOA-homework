#1

# Implicit Conversion (არაპირდაპირი გარდაქმნა)
# ეს არის გარდაქმნა, რომელსაც Python თვითონ აკეთებს Programmer-ის გარეშე.
# ხდება ავტომატურად, როცა პატარა ტიპი გადაინაცვლებს დიდზე და მონაცემი არ იკარგება.

a = 5        
b = 2.5      
c = a + b    # Python ავტომატურად გადააქცევს a-ს float-ს  implicit conversion
print(c)     

# Explicit Conversion (პირდაპირი გარდაქმნა)
# როცა ტიპის შეცვლას Programmer თავად აკეთებს კონკრეტული ფუნქციის გამოყენებით.
# მაგალითად int(), float(), str(), list() და ა.შ.

x = "25"         
y = int(x)       # სტრინგს ხელით ვაქცევთ int-ად → explicit conversion
print(y + 5)     

#2 int
x = "15"
y = int(x)
print(y)      

#2 float

x = "3.14"
y = float(x)
print(y)      # 3.14 (float)

#2 str
x = 50
y = str(x)
print(y)      # "50" (string)

#2 boolean
print(bool(1))      # True
print(bool(0))      # False
print(bool("hi"))   # True
print(bool(""))     # False

#3
num = 6/2
print(type(num))   # <class 'float'>

#4
number = 6.0
number > 6   # False


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

result = a // b
print(result)   # შედეგი იქნება ინტეგერი







