# Compress a string - has to be case sensitive. AAAAaaBBBCc -> A4a2B3C1c1. AKA. Run length compression algorithm

def compress_b(s):
    s = [i for i in s if i]
    s.sort()
    d = dict({s[0]:1})
    count = 1
    current = [s[0]]
    for i in s[1:]:
        if i == current:
            count += 1
        else:
            d.update({})
            current = i
    return type(d)
# didn't work too complex


def compress(s):
    r = ''
    l = len(s)

    if l == 0:
        return ''
    if l == 1:
        return s+"1"
    last = s[0]
    cnt = 1

    i = 1

    while i < l:
        if s[i] == s[i-1]:
            # if current element is equal to the previous element
            cnt +=1
        else:
            r = r + s[i-1] + str(cnt)
            cnt = 1

        i += 1
    r = r + s[i-1] + str(cnt)
    return r
# Doesn't sort in alphabetical order
print(compress('AAAAaaBvBBCc'))
