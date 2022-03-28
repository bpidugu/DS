# LinkedList Data Structure



from sre_constants import CATEGORY_WORD



class LinkedList:
    def __init__(self,value):
        self.value = value
        self.next = None

    def addMany(self, values):
        current = self
        while current.next is not None:
            current = current.next
        for value in values:
            current.next = LinkedList(value)
            current = current.next
        return self
# linkedListOne = 2->4->7->1
# linkedListTwo = 9>4->5
# output = 1->9->2->2
    def sumofLinkedList(linkedListOne, linkedListTwo):

        newLLPointer = LinkedList(0)
        currNode = newLLPointer
        carry =0


        nodeOne = linkedListOne
        nodeTwo = linkedListTwo

        while nodeOne is not None  or nodeTwo is not None:
            valueOne = nodeOne.value if nodeOne is  not None else 0
            valueTwo = nodeTwo.value if nodeTwo is  not None else 0
            sum_vals = valueOne + valueTwo + carry

            newValue= sum_vals % 10
            newNode = LinkedList(newValue)
            currNode.next = newNode
            currNode = newNode

            carry = sum_vals//10
            nodeOne = nodeOne.next if nodeOne is not None else None
            nodeTwo = nodeTwo.next if nodeTwo is not None else None

        return newLLPointer.next



if __name__ == "__main__":
    main()

