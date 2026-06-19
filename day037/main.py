# 0

# .add() - გამოიყენება სეტში ელემენტის ცასამატებლად
# .update() - გამოიყენება სეტის მნიშვნელობის გასანახლებლად
# .remove() - გადავცემთ იმ ელემენტს რომლის წაშლაც გვინდა სეტიდან მარამ გვიერორებს
# .discard() - გადაეცემა ელემენტი რომლის წაშლაც გვინდა სეტიდან მაგრამ არ გვიერორებს
# .pop() - სეტის რანდომულ ელემენტს შლის
# .clear() - სეტის ყველა ელემენტს შლის
# .union() - ორი სეტის შეეrtებისთვის გამოიყენება
# .intersection() - საერტო ელემენტებს ვიღებთ 2 განსხვავებული სეტიდან
# .difference() - გვიბრუნებს სეტის უნიკალურ ელემენტს
# .simetric_difference() - ორი სეტის ჯამს აბრუნებს


# 1

# .remove() - გადავცემთ იმ ელემენტს რომლის წაშლაც გვინდა სეტიდან მარამ გვიერორებს
# .discard() - გადაეცემა ელემენტი რომლის წაშლაც გვინდა სეტიდან მაგრამ არ გვიერორებს


# 2

names = {"saba" , "vano" , "luka"}

names.add("nika")
names.discard("giorgi")


# 3

# car1 = {"bmw" , "honda" , "mercedes" , "hyundai"}
# car2 = {"bmw" , "toyota" , "honda" , "subaru"}

# x = car1.intersection(car2)

# print(x)

# # 4

# y = car1.union(car2)

# print(y)

# # 5

# drinks = {"cola" , "nataxtari" , "borjomi" , "fanta"}
# i = drinks.remove("cola")

# print(drinks)

# # 6

# name1 = {'nika' , 'vano' , 'giorgi', 'luka' , 'bizina_ivanishvili'}
# name2 = {'nika', 'zarzura', 'bizina_ivanishvili' , 'saba'}

# o = name1.difference(name2)

# print(o)

# # 7

# b = name1.symmetric_difference(name2)

# print(b)

# # 8

# surname = {'patarkalashvili', 'motiashvili', 'boyoveli'}

# g = surname.clear()                 

# print(surname)