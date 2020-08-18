"""
Read Numbers a,b,c,d with condn 1<=a,b,c,d<=1000.
Print sum of a^b and c^d
"""
 
def IntegerComesInAllSizes(a,b,c,d):
    if 1<=a<=1000 and 1<=b<=1000 and 1<=c<=1000 and 1<=d<=1000:
        return pow(a,b)+pow(c,d)
a=int(input("Enter a ")) 
b=int(input("Enter b "))
c=int(input("Enter c "))
d=int(input("Enter d "))
print(IntegerComesInAllSizes(a,b,c,d))
