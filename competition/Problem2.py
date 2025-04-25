"""
You have to decorate a christmas tree.
You have given B number of balls and C number of candles and A number of balloons.
And You are given N that represent how many items you have to use.
You have to find out all the possible combinations of items you can use to decorate the tree.

Ex1:
N=2
B=0
C=1
A=1
Output: "CA AC"

Ex2:
N=3
B=1
C=1
A=1
Output: "BCA BAC CBA CAB ABC ACB"
"""

from itertools import combinations, permutations

def sort_strings(str_list):
    weight = {'B': 0, 'C': 1, 'A': 2}
    return sorted(str_list, key= lambda s: [weight[c] for c in s])

def get_decorations(N, B, C, A):
    balls="B"*B
    candles="C"*C
    balloons="A"*A

    all_items=balls+balloons+candles
    print(all_items)

    possible_way=permutations(all_items, N)

    ways=["".join(e) for e in possible_way]
    print(ways)

    ways = sort_strings(ways)

    for way in ways:
        print(way, end=" ")



if __name__=="__main__":
    N,B,C,A=2,0,1,1
    get_decorations(N, B, C, A)