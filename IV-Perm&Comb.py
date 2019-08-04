# # # Combination # # #

# Example
# For several given letters, print out all the combination of it's letters
# Input: 1 2 3
# Output: 1 2 3
#         1 3 2
#         2 1 3
#         2 3 1
#         3 1 2
#         3 2 1
from itertools import permutations,combinations

def comb(n,*args):
    _list = []
    for letter in args:
        _list.append(letter)
    perm = permutations(_list)
    comb = combinations(_list, n)
    for p in perm:
        print(p)
    print("============")
    for c in comb:
        print(c)

comb(3, 3,1,2)
