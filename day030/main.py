# 1
def two_sort(array):
    
    array = sorted(array)
    
    first_word = array[0]
    
    result = "" 
    
    
    for i in first_word:
        result += i + "***"
    
    return result[0:-3]

# 2

def no_boring_zeros(n):
    
    if n == 0:
        return 0
    
    while n % 10 == 0:
        n //= 10
    
    return n

# 3

def is_palindrome(s):
    
    if s.lower() == s[::-1].lower():
        return True
    else:
        return False
    

# 4

def find_needle(haystack):
    
    
    
    
    for i in haystack:
        if i == 'needle':
            return f"found the needle at position {haystack.index(i)}"
        else:
            continue

# 5

def is_isogram(string):
    
    already = ""
    
    for i in range(0,len(string)):
        
        if string[i].lower() in already:
            return False
        else:
            already += string[i].lower()
    
    return True

# 6

def to_jaden_case(string):
    
    appended = ''
    
    splited = string.split(' ',)
    
    for i in splited:
        appended += i.capitalize() + ' '
    
    return appended[:-1]