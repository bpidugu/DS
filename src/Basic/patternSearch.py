
def isMatch(w,p):
    lenW = len(w)
    lenP = len(p)
    if (lenW >0 and lenW == lenP):
        for i in range(lenW):
            if(w[i] == p[i] or p[i] =="anything"):
                continue
            else: return False
        return True
    return False



def IsPatternInOrder(words, patterns):
    if(words is None or patterns is None): return 0

    lenP = len(patterns)
    lenW = len(words)
    op = [0]* lenP
    idx = 0
    idy = 0
    for p in patterns:
        m = len(p)
        while idx <= (lenW-m):
            print(idx,m)
            if isMatch(words[idx:m+idx],p):
                op[idy] = 1
                idx +=1
                idy +=1
                break
            idx +=1
    return op

w = ["banana","apple","apple","orange","cherry","apple","cherry","orange"]
p = [["apple","apple"],["cherry","apple","cherry"]]

f =IsPatternInOrder(w,p)
print(f)

result = all(element == 1 for element in f)
print (result)