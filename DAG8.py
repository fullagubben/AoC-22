import numpy as np

my_file = open("LIST8.txt", "r")
data = my_file.read() 
forest = data.split("\n")

tempnumberlist = []


def checksize(forest):
    columns = 0
    rows = len(forest[0])
    for trees in forest:
        columns += 1
    return rows,columns

rangerows = checksize(forest)[0]
rangecolumns = checksize(forest)[1]



treelistnew = []
for tree in forest:
    tempnumberlist.append(list(tree))

A = np.array(tempnumberlist)
for rows in range(0,rangerows):    # VÄNSTER TILL HÖGER
    tempold = -1
    for columns in range(0,rangecolumns):
        tempnew = A[rows][columns]
        if str(tempnew) > str(tempold):
            treelistnew.append([rows,columns])
            tempold = tempnew


for columns in range(0,rangecolumns):              # UPP TILL NER
    tempold = -1
    for rows in range(0,rangerows):
        tempnew = A[rows][columns]
        if str(tempnew) > str(tempold):
            treelistnew.append([rows,columns])
            tempold = tempnew




for rows in range(0,rangerows):                 # HÖGER TILL VÄNSTER
    tempold = -1
    for columns in reversed(range(0,rangecolumns)):
        tempnew = A[rows][columns]
        if str(tempnew) > str(tempold):
            treelistnew.append([rows,columns])
            tempold = tempnew



for columns in range(0,rangecolumns):              # NERIFRÅN TILL UPP
    tempold = -1
    for rows in reversed(range(0,rangerows)):
        tempnew = A[rows][columns]
        if str(tempnew) > str(tempold):
            treelistnew.append([rows,columns])
            tempold = tempnew




res = []
[res.append(x) for x in treelistnew if x not in res]

print(len(res))



#----------------- PART 2 ------------------------------



def find_best_tree(tree):
    numcolumn = checksize(tree)[1]    
    totrows = checksize(tree)[0]  
    totscore = 0
    for row in range(totrows):    
        for col in range(numcolumn):
            height = tree[row][col]
            up = down = left = right = 0

            for r in range(row - 1, -1, -1):    # Ner till upp
                if tree[r][col] >= height:
                    up += 1
                    break
                up += 1  

            for r in range(row + 1, totrows):    # Upp till ner
                if tree[r][col] >= height:
                    down += 1  
                    break
                down += 1  

            for c in range(col - 1, -1, -1):     # Höger till vänster
                if tree[row][c] >= height:
                    left += 1  
                    break
                left += 1  

            for c in range(col + 1, numcolumn):    # Vänster till höger
                if tree[row][c] >= height:
                    right += 1  
                    break
                right += 1   
            totscore = max(totscore, up*left*down*right)
    return totscore
    
print(find_best_tree(A))




