import math


def encodeByOrientation(string, row):
    d = row -1
    emptyCells = (d*(d+1))/2
    totalChars = emptyCells + len(string)
    cols = math.ceil(totalChars/row)
    op = [['_' for i in range(cols)] for j in range(row)]
    
    idx_i =0
    idx_j=0
    incr=0
    for c in string:
       # print(idx_i,idx_j)

        op[idx_i][idx_j] = c
        #print(op[idx_i][idx_j])
       
        if(idx_i == row-1):
            #print("rotate")
            incr +=1
            idx_i = 0
            idx_j = incr
        else:
            idx_i +=1
            idx_j +=1
    a = ""
    for i in range(len(op)):
        for j in range(len(op[i])):
            c = op[i][j]
            if(c == ' '):
                c = '_'
           
            a += c
           
        
    print(a)
    return a
  

'''
(0,0) (0,1) (0,2) (0,3) (0,4)
(1,0) (1,1) (1,2) (1,3) (1,4)
(2,0) (2,1) (2,2) (2,3) (2,4)


(0,0) (0,1) (0,2) (0,3) (0,4)
(1,0) (1,1) (1,2) (1,3) (1,4)
(2,0) (2,1) (2,2) (2,3) (2,4)
(3,0) (3,1) (3,2) (3,3) (3,4)
(4,0) (4,1) (4,2) (4,3) (4,4)

'''

def decode(string,row):
    #cnt = len(string)
    col = math.ceil(len(string)/row)
    op = [['_' for i in range(col)] for j in range(row)]
    print(op)
    idxI=0
    idxJ=0
    incr =0 
    for c in string:
        print(c)
        op[idxI][idxJ] = c
        if(idxJ == col-1):
            print('next')
            idxJ =0
            incr += 1
            idxI = incr
        else:
            idxJ +=1
            
    a = ""
    # TODO:
    for i in range(len(op)):
        for j in range(len(op[i])):
            c = op[i][j]
            if(c == ' '):
                c = '_'
           
            a += c

    print(op)
    return a
    pass


    


if __name__ == "__main__":
    encodeByOrientation("my name is",3)
    s = encodeByOrientation("hello world",2)
    decode(s,2)
    