# 1 Arrays Udemy Course

def anagram(st1,st2):
    a = sorted(str(st1).lower().replace(' ', ''))
    b = sorted(str(st2).lower().replace(' ', ''))
    return a == b

# hash table method using dict. Bloody long!

def anagram2(st1, st2):
    st1 = st1.lower().replace(" ", "")
    st2 = st2.lower().replace(" ", "")
    if len(st1) != len(st2):
        return False

    count = {}

    for letter in st1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1

    for letter in st2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1

    for k in count:
        if count[k] != 0:
            return False
    return True

st1 = 'gooood'
st2 = 'dog '

print(anagram2(st1, st2))
