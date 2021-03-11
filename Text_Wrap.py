# Text Wrap

"""
You are given a string S and width W. 
Your task is to wrap the string into a paragraph of width W.

Input Format

The first line contains a string, S. 
The second line contains the width, W.

Sample Input::
ABCDEFGHIJKLIMNOQRSTUVWXYZ
4

Sample Output::
ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ

"""

import textwrap

def wrap(string, max_width):
	return "\n".join(string[i:i+max_width] for i in range(0,len(string),max_width))
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)