# Dictionary Data Structure


# Sory the array descending transaction count, then ascending alphabetically by item name with matching transaction Counts
# input => transactions ["notebook, "mouse","keyboard","mouse","notebook"]
# output => ["mouse 2", "notebook 2", "keyboard 1"]

# def getTransactions(txns):

#     d = {}
#     for txn in txns:
#         if d[txn] is None:
#             d[txn] = 1
#         else:
#             cnt = d[txn]
#             d[txn] = cnt +1
    
#     sorted_dict = sorted (d.values())
#     sorted_dict = sorted (d.values())


def dictionary():
    key_val = {}

    key_val["notebook"] = 2
    key_val["sketchboard"] = 1
    key_val["mouse"] = 2
    key_val["orange"] = 2
    key_val["orange1"] = 4
    key_val["orange2"] = 3
    key_val["apple"] = 1
   
    print(sorted(key_val.items(), key = lambda kv:(-kv[1], kv[0])))
   # sl = sorted(key_val.items(), key = lambda kv:(kv[1]),reverse=True).sort(key= lambda)
    #print(sorted(key_val.items(), value = lambda kv:(kv[0], kv[1])))
    #print(sorted(key_val.items()))
    #print(sl)

    for i in range(len(key_val)):
        print(i)
    print("REVERSED.....")
    for i in reversed(range(len(key_val))):
            print(i)


class LinkedList:
    def __init__(self,value):
        self.value = value
        self.next = None

# linkedListOne = 2->4->7->1
# linkedListTwo = 9>4->5
# output = 1->9->2->2
def sumofLinkedList(linkedListOne, linkedListTwo):
    nodeOne = linkedListOne
    nodeTow = linkedListTwo
    carry = 0
    newLinkedList = LinkedList(0)
    currNode = newLinkedList

    pass
def main():
    dictionary()


if __name__ == "__main__":
    main()

