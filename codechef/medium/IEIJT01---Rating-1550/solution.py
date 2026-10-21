class Node:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.next = None
        self.prev = None
        
class LruCache:
    def __init__(self, cacheCapacity):
        self.cacheCapacity=cacheCapacity
        self.cache={}
        self.head=Node(0,0)
        self.tail=Node(0,0)
        self.head.next=self.tail
        self.tail.prev=self.head
    def insert(self,node):
        node.next=self.head.next
        self.head.next.prev=node
        self.head.next=node
        node.prev=self.head 
    def remove(self,node):
        nextnode=node.next
        previ=node.prev
        previ.next=nextnode
        nextnode.prev= previ
    def getValue(self, cacheKey: int) -> int:
        if cacheKey not in self.cache:
            return -1
        node=self.cache[cacheKey]
        self.remove(node)
        self.insert(node)
        return node.value
    def putValue(self, cacheKey: int, cacheValue: int) -> None:
        node=Node(cacheKey,cacheValue)
        if cacheKey in self.cache:
            self.remove(self.cache[cacheKey])
            del self.cache[cacheKey]
        self.cache[cacheKey]=node
        self.insert(node)
        if self.cacheCapacity<len(self.cache):
            x=self.tail.prev
            self.remove(x)
            del self.cache[x.key]
        