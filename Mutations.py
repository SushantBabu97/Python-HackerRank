#Mutations

"""
We have seen that lists are mutable (they can be changed), and tuples are immutable (they cannot be changed).
Let's try to understand this with an example.
You are given an immutable string, and you want to make changes to it.

Input Format::
The first line contains a string, s. 
The next line contains an integer i, denoting the index location and a character  separated by a space.

Sample Input::
abracadabra
5 k

Sample Output::
abrackdabra

"""

def mutate_string(string, position, character):
    return s[:int(i)]+c+s[int(i)+1:]

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)