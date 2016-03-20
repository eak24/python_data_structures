class BinHeap:
    # BinHeap creates a balanced binary tree based on some comparator... could be min or max or whatever.
    # Heap invariant is that comparator(new_item,parent(new_item))=true == comparator(parent(new_item), new_item)=false
    # [0,1,2,3,4,5]
    def __init__(self, comparator):
        self.heapList = [0]
        self.comparator = comparator
        self.currentSize = 0

    def insert(self, item):
        self.heapList = self.heapList + [item]
        self.currentSize += 1
        self.percolate_up(self.currentSize)

    def percolate_up(self, i):
        while i // 2 > 0:
            if self.comparator(self.heapList[i // 2], self.heapList[i]):
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i // 2

    # If the node at i is greater than its children, switch with smallest child
    def percolate_down(self, i):
        while i*2+1<=self.currentSize:


    def remove(self):
        self.heapList

import unittest
import random
class TestHeapPlay(unittest.TestCase):
    def greater_than(i,j):
        return i > j
    print(greater_than(4,5))

    random_list=random.sample(range(1000),100)

    bin_heap=BinHeap(greater_than)

    print(random_list)

    for i in random_list:
        bin_heap.insert(i)
        print(bin_heap.heapList)

if __name__ =='__main__':
    unittest.main()