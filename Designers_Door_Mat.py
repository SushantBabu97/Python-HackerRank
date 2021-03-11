"""
Sample Input::
9 27

where n=9 and m=27

Sample Output::

------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
----------WELCOME----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------
"""

n,m=map(int,input().split())
c='.|.'         
for i in range(1,n,2):
	print((c*i).center(m,'-'))     #range returns [1,3,5] for n=7 as range is upto n-1  
print('WELCOME'.center(m,'-'))
for i in range(n-2,-1,-2):         #range reaches one step ahead of -1>>0, n-2 because (n-1)/2 times to be printed 
	print((c*i).center(m,'-'))