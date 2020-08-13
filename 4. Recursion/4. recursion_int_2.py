# python has a itertools library that does this for you

def permut(s, out=None):
    if out is None:
        out = []

    if s in out:
        return out
    else:
        out.append(s)
        return permut((s[-1] + s[:-1]), out)

# my attempt didn't solve all possible versions

"""
1. iterate through first string
2. for each character in the initial string, set aside that character and get a list
    of all the possible permutations of that string that's left.
3. Once done, add each variations to the list to the character, and add those to final list
4. return final list
"""

def permute(s):
    out = []

    if len(s) == 1:
        out = [s]
    else:
        # for every letter in string
        for i,let in enumerate(s):
            # for every permutation resulting from Step 2 and 3
            for perm in permute( s[:i] + s[i+1:] ):
                print('Current letter is: ', let)
                print('Perm is: ', perm)
                out += [let+perm]

    return out

print(permute('abc'))
