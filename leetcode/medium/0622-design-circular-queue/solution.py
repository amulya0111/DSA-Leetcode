class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
class MyCircularQueue(object):

    def __init__(self, k):
        self.head = None
        self.tail = None
        self.k = k
        self.count = 0
    def enQueue(self, value):
        n=Node(value)
        if self.k==self.count:
            return False
        if self.count==0:
            self.head=self.tail=n
            self.tail.next = self.head
        else:
            self.tail.next=n
            self.tail=n
            self.tail.next = self.head
        self.count+=1
        return True
        

    def deQueue(self):
        if self.count==0:
            return False
        else:
            self.head=self.head.next
            self.count-=1
            if self.count==0:
                self.head=self.tail=None
            else:                
                self.tail.next = self.head
            return True

    def Front(self):
        """
        :rtype: int
        """
        if self.count==0:
            return -1
        return self.head.val
        

    def Rear(self):
        """
        :rtype: int
        """
        if self.count==0:
            return -1
        return self.tail.val
        

    def isEmpty(self):
        return self.count==0
        

    def isFull(self):
        return self.count==self.k
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()