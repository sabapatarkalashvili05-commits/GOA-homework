# 0

# fruits = {"apple" , 'banana' , "peach" , 'pear' }

# fruits.add("grape")


# 1

colors = {'green' , 'red' , 'blue' , 'black' , 'white'}

colors.remove('green')

print(colors)

# 2

animals = input('please enter 3 animals:  ')

animals =  set(animals)

animals.clear()

# 3

group1 = {"Ana", "Gio", "Nika"} 
group2 = {"Nika", "Luka", "Saba"}

group1.intersection(group2)

# 4

A = {1, 2, 3, 4} 
B = {3, 4, 5, 6}

print(A.intersection(B)) # გამოიტანს A და B სეტში მყოფ საერთო ელემენტებს :3
print(A.union(B)) # გამოიტანს შეერთებულ სეტს A და B ელემენტებისგან :3
print(A.difference(B)) # გვიბრუნებს პირველი სეტის უნიკალურ ელემენტს :3
print(A.symmetric_difference(B)) # გვიბრუნებს ორი სეტის ჯამს დუპლიკატები გარეშე :3