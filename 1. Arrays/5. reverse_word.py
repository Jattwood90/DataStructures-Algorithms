# Reverse a string and remove trailing spaces
# My solution

def reverse(string):
    new = list(string.split(' '))
    new = [x for x in new if x] # cool way of filtering spaces out from a list
    new = reversed(new)
    final = " ".join(new)
    return final


# One line solutions - avoid doing these in an interview setting

def rev_word(s):
    return " ".join(reversed(s.split()))

def rev_word2(s):
    return " ".join(s.split()[::-1])



# Manual Solution
def rev_manual_word(s):

    words = []
    length = len(s)
    spaces = [' ']

    i = 0

    while i < length:
        if s[i] not in spaces:
            word_start = i

            while i < length and s[i] not in spaces: # i referes to the element of the list in s
                i+=1
            words.append(s[word_start:i])
        i +=1

    return " ".join(reversed(words))


print(rev_manual_word('   This is    a string     '))