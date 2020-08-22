"""
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given n scores. Store them in a list and find the score of the runner-up.

For list [2,3,6,6,5] print 5 as it is the second largest score.
"""


from collections import Counter
if __name__ == '__main__':
    n = int(input())
    arr = list(set(map(int, input().split())))
    arr.remove(max(arr))
print(max(arr))

"""
----------------------OR-----------

from collections import Counter
if __name__ == '__main__':
    n = int(input())
    arr = list(set(map(int, input().split())))
    arr.sort()
print(arr[-2])
"""
