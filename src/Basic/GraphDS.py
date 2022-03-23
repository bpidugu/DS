# Graph Data Structures

# stack data structure 

from array import array
from logging import root
from re import L


class Node:
    def __init__(self, name):
        self.children = []
        self.name = name
    
    def addChild(self, name):
        self.children.append(Node(name))
        return self
    
    def DFS(self, array):
        #Stack
        array.append(self.name)
        print(self.name)
        for c in self.children:
            c.DFS(array)
        return array

    def BFS(self,array):
        #queue
        que = [self]
     
        while len(que) >0:
            curr = que.pop(0)
           
            array.append(curr.name)
            for c in curr.children:
                que.append(c)
        
        return array



def run():
   
    rootNode = Node("A")
    cB = Node("B")
    cC = Node("C")
    cD = Node("D")
    cE = Node("E")
    cF = Node("F")


    cD.children.append(cF)
    cB.children.append(cD)
    cC.children.append(cE)
   
    rootNode.children.append(cB)
    rootNode.children.append(cC)
  

    k =[]
    rootNode.DFS(k)

    print("DFS>>>>")
    print(k)
    
    b=[]
    rootNode.BFS(b);
    print("BFS>>>>")
    print(b)


if __name__=="__main__":
    run();


