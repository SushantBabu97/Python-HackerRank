#Find a string

"""
In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.

Sample Input::
ABCDCDC
CDC

Sample Output:
2

"""

def count_substring(string, sub_string):
    ct=0
    while sub_string in string:
    	i = string.find(sub_string)
    	string = string[i + 1:]
    	ct += 1
    return ct

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)