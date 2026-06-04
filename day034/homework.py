# 1

# Set-იც და Tuple-იც მონაცემთა ტიპებია Python-ში:ორივეს შუძლია რამდენიმე ელემენტის ერთ ცვლადში შენახვა,ორივეს შეუძლია რამდენიმე ელემენტის ერთ ცვლადში შენახვა,# ორივე შეიძლება გამოყენებულ იქნას მონაცემების დასაჯგუფებლად და შესანახად

# 2



tuple = (1,2,3,4,5)


(tuple1,tuple2,*tuple3) = tuple

print(tuple1)
print(tuple2)
print(tuple3)


# 3

set = {"საბა","ნიკა","გიორგი","ლაშა"}

user_input = input("გთოხ შეიყვანე შენი სახელი:  ")


for user_input in set:
    if user_input in set:
        print("ეს სახელი არის სეტში და აღარ დაემატება")
    else:
        set.add(user_input)

print(set)


# 4


# thistuple = ("vano", "saba", "giorgi")
# y = list(thistuple)
# y.append("luka")
# thistuple = tuple(y)





thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
