# Binary Search
# O(log(n)) - search, insert, update and delete


class BstNode:
    def __init__(self, val=None) -> None:
        self.left = None
        self.right = None
        self.val= val
    
    def insert(self, val):

        if not self.val:
            self.val = val
            return
        if self.val == val:
            return
        
        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BstNode(val)
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = BstNode(val)
    
    # Delete

    def delete(self, val):

        if self == None:
            return self
        
        if val < self.val:
            

    # Get MIN
    def getMin(self):
        current = self
        while current.left is not None:
            current  = current.left
        
        return current.val
    
    # Get MAX

    def getMax(self):
        current  = self
        while current.right is not None:
            current = current.right
        return current.val

    # Val exists

    def exists(self, val):

        if (val == self.val):
            return True
        
        if val < self.val:
            if self.left == None:
                return False
            return self.left.exists(val)
        
        if self.right == None:
            return False
        return self.right.exists(val)
    
    # InOrder - Lef,Root,Right
    def inorder(self, vals):
        if self.left is not None:
            self.left.inorder(vals)
        if self.val is not None:
            vals.append(self.val)
        if self.right is not None:
            self.right.inorder(vals)
        return vals

    # PreOrder - Root, L,R
    def preorder(self, vals):
        if self.val is not None:
            vals.append(self.val)
        if self.left is not None:
            self.left.preorder(vals)
        if self.right is not None:
            self.right.preorder(vals)
        return vals
    
    # PostOrder - L,R, Root
    def postorder(self, vals):    
        if self.left is not None:
            self.left.postorder(vals)
        if self.right is not None:
            self.right.postorder(vals)
        if self.val is not None:
            vals.append(self.val)
        return vals


def main():
    nums = [23,45,5,6,8,9,55,17,22,18,32,9]

    bst = BstNode()

    for num in nums:
        bst.insert(num)
    
    print("InOrder")
    print(bst.inorder([]))
    print("#######")
    print("PreOrder")
    print(bst.preorder([]))
    print("#######")
    print("PostOrder")
    print(bst.postorder([]))
    print("#######")


if __name__ == "__main__":
   main()

        

"""
Insert new Record
"""

 
