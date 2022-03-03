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

(i,j)
(0,0) (0,1) (0,2) (0,3) (0,4)
(1,0) (1,1) (1,2) (1,3) (1,4)
(2,0) (2,1) (2,2) (2,3) (2,4)
(3,0) (3,1) (3,2) (3,3) (3,4)
(4,0) (4,1) (4,2) (4,3) (4,4)

'''

def decode(string,row):
    #cnt = len(string)
    if(string is None): return None
    if(len(string) <=3): return string
    

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
           
            idxJ =0
            incr += 1
            idxI = incr
        else:
            idxJ +=1
            
    a = ""
    # TODO:
    idxI=0
    idxJ=0
    incr =0
    diag = 0
    for i in range(row*col):
        print(idxI,idxJ)
        c = op[idxI][idxJ]
        if(c == '_'): c = ' '
        
        a += c
        diag += 1
        if (idxI==0 and idxJ==col-1):
            break;
        if(diag == row or idxJ==col-1):
            print('next')
            idxI =0
            incr +=1
            idxJ = incr
            diag = 0
        else:
            idxI +=1
            idxJ +=1

    print(a)
    return a



    


if __name__ == "__main__":
    s = encodeByOrientation("my name is",3)
    s1= encodeByOrientation("hello world",2)
    en1= encodeByOrientation("benjamin is krupakar",2)
    decode(s,3)
    decode(s1,2)
    dc1 = decode(en1,2)
    print(en1,dc1)
   
    


