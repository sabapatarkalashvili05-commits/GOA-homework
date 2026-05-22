# 1

def split_clone(string,splitsymbol):
    
    result = []
    symbol = ''

    for i in string:
        if i == splitsymbol:
            result.append(symbol)
            symbol = ''
        else:
            symbol += i

    result.append(symbol)
    return result


print(split_clone('hello world', " "))
print(split_clone('hello.world.how.are.you', "."))


# 2

def join_clone(list,joinsymbol):


    string = ''



    for i in list:
        string += i
        string += joinsymbol
    string = string[0:-1]
    return string


print(join_clone(['1','5','1','3'], '$'))



print('$'.join(['1','5','1','3']))

# 3

def smash(words):
    
    return ' '.join(words)


# 4

def digitize(n):
    
    n = str(n)
    
    n = n[::-1]
    
    
    digit = []
    
    for i in n:
        digit.append(int(i))
    
    
    return digit