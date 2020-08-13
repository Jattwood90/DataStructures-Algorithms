"""
Recursion if a method of expressing a recursive function towards the base case. Maybe.
An example of this is n! (factorial) or n! = n * (n-1), if n= 0*n! = 1 (or base case)
"""

def fact(n):

    # base case
    if n == 0:
        return 1
    else:
        return n * fact(n-1)


def recsum(n):
    if n == 0:
        return 0
    else:
        return n + recsum(n-1)

def sum_func(n):
    # receives a recursion error?

    if len(str(n)) == 1:
        return n
    else:
         #strip another digit
        return n%10 + sum_func(n/10)

def word_split(phrase, wordlist, output=None):
    if output is None:
        output = []
#this base case takes care of creating an empty list in the first instance of the recursion

    for word in wordlist:

        if phrase.startswith(word):
            output.append(word)

            return word_split(phrase[len(word):], wordlist, output)
    return output

print(word_split('themanran', ['man', 'ran']))
