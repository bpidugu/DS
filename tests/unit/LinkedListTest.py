

import unittest
from src.Basic.LinkedListDs import LinkedList



def getNodesInArray(output):
    nodes = []
    current = output
    while current is not None:
        nodes.append(current.value)
        current = current.next
    return nodes


class TestProgram(unittest.TestCase):
    def test_case_1(self):
       
        ll1 = LinkedList(2).addMany([4, 7, 1])
        ll2 = LinkedList(9).addMany([4, 5])
        expected = LinkedList(1).addMany([9, 2, 2])
        actual = LinkedList.sumofLinkedList(ll1, ll2)
        
        self.assertEqual(getNodesInArray(actual), getNodesInArray(expected))


if __name__ == '__main__':
    unittest.main()

