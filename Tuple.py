# Tuples

"""
Given an integer, n, and n space-separated integers as input, create a tuple, t, 
of those n integers. Then compute and print the result of hash(t).

hash()  is a builtin function.
"""

if __name__ =='__main__' :
	n=int(input())
	integer_list=list(map(int,input().split()))
	t=tuple(integer_list)
	print(hash(t))

