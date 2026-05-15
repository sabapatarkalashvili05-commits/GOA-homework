# 1


def squeare(x):
    return x * x


print(squeare(12))


# 2

def number(x):
    if x % 2 == 0:
        return "ლუწია"
    else:
        return "კენტია"


print(number(25))


# 3

def palindrom(word):
    if word == word[::-1]:
        return "palindrom"
    else:
        return "no palindrom"

print(palindrom("level"))  # palindrum
print(palindrom("hello"))  # no palindrom


# 4

def numbers(numbers):
    new_list = [0]
    for num in numbers:
        if num % 2 == 0:
            new_list.append(num)
    return new_list

print(numbers([1, 2, 3, 4, 5, 6]))

# 5

def longest_word(words):
    longest = words[0]
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest


print(longest_word(["hello", "elephan", "dog", "lizzard"]))