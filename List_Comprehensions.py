"""
Let's learn about list comprehensions! You are given three integers x,y and z representing
the dimensions of a cuboid along with an integer n. Print a list of all possible coordinates
given by (i,j,k) on a 3D grid where the sum of i+j+k is not equal to n. Here, 0<=i<=x;0<=j<=y;
0<=k<=z. Please use list comprehensions rather than multiple loops, as a learning exercise.


Example::

x=1,y=1,z=2,n=3

All permutations of [i,j,k] are:
[[0,0,0],[0,0,1],[0,0,2],[0,1,0],[0,1,1],[0,1,2],[1,0,0],[1,0,1],[1,0,2],[1,1,0],[1,1,1],[1,1,2]]

Since, n=3, i+j+k !=3
[[0,0,0],[0,0,1],[0,0,2],[0,1,0],[0,1,1],[1,0,0],[1,0,1],[1,1,0],[1,1,2]]

"""



if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    x_list=[x for x in range(x+1)]
    y_list=[y for y in range(y+1)]
    z_list=[z for z in range(z+1)]

    Permutations=[[i,j,k] for i in x_list for j in y_list for k in z_list if i+j+k!=n]
    
    print(Permutations)


"""
Alternatively,
print ([[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i + j + k != n ])
"""




"""
>> ListOfNumbers = [ x for x in range(10) ] # List of integers from 0 to 9
>> ListOfNumbers
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


>>> print([[x, y] for x in [1, 2, 3] for y in [4, 5, 6]])
[[1, 4], [1, 5], [1, 6], [2, 4], [2, 5], [2, 6], [3, 4], [3, 5], [3, 6]]


>> ListOfThreeMultiples = [x for x in range(10) if x % 3 == 0] # Multiples of 3 below 10
>> ListOfThreeMultiples
[0, 3, 6, 9]
"""



