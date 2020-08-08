# return true or false if a string is comprised of a unique set of characters, e.g 'abcde'
# My solution
def unique(s):
    if len(s) ==0:
        return False

    s = [i for i in s]
    count = [s[0]]
    for i in s[1:]:
        if i in count:
            return False
        else:
            count.append(i)
    return True


# One line special Python method answer
def uni_char(s):
    return len(set(s)) == len(s)

# Second solution. Much more efficient than my solution, as I converted a str to a list.
def uni_char2(s):
    char = set()
    
    for let in s:
        if let in char:
            return False
        else:
            char.add(let)
    return True
print(uni_char('abc'))
