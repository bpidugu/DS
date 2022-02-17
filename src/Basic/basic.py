#1. Arithmetic Operations: Integet & Float Division,  and modular arithmetic
#2. Language Elements: Branching, Loops, Keyowrds and Functions
#3. Data Structures: Integer, Float, String, Lists, Set, Dictionary, & Graph
#4. Sequence Operators: Indexing, Concatenation, Slicing, and Build-In functions
#5. Function Arguments: default, aribitrary, unpacking, Keyword
#6. Set Operations: Lambda, Filter, map, and intersection functions
#7. Algorithms: recursion, Fibionacci, BSearch, Sorting, Guess & Check, and Graph Traversal


a = [ [2, 4, 6, 8 ], 
    [ 1, 3, 5, 7 ], 
    [ 8, 6, 4, 2 ], 
    [ 7, 5, 3, 1 ] ] 
          
for i in range(len(a)) : 
    for j in range(len(a[i])) : 
        print(a[i][j], end=" ")
    print() 


m = 4
n = 5
  
a = [[False for x in range(n)] for x in range(m)]
print(a)