#Nested List

"""
Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Example:: 

records=[["chi",20.0],["beta",50.0],["alpha",50.0]]

The ordered list of scores is [20.0,50.0], so the second lowest score is 50.0. There are two students with that score: . Ordered alphabetically, the names are printed as:
["beta","alpha"]
alpha
beta
"""
if __name__ == '__main__':
    a=[]
    sl_name=[]
    scores=set()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        a.append([name,score])
        scores.add(score)

    sl=sorted(scores)[1]

    for name,score in a:
    	if score==sl:
    		sl_name.append(name)
    for name in sorted(sl_name):
    	print(name,end='\n')






"""
set() eliminates duplicate item. set([1,2,3,1]) gives [1,2,3].
"""