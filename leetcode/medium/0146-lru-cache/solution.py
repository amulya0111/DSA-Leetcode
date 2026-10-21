
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}

        # Dummy head and tail
        self.head = Node(0, 0)
        self.tail = Node(0, 0)

        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

    def insert(self, node):
        next_node = self.head.next

        self.head.next = node
        node.prev = self.head

        node.next = next_node
        next_node.prev = node

    def get(self, key):
        if key not in self.cache:
            return -1

        node = self.cache[key]

        # Mark as most recently used
        self.remove(node)
        self.insert(node)

        return node.value

    def put(self, key, value):
        # If key exists, remove its old node
        if key in self.cache:
            self.remove(self.cache[key])

        node = Node(key, value)
        self.cache[key] = node
        self.insert(node)

        # Evict least recently used if over capacity
        if len(self.cache) > self.capacity:
            lru = self.tail.prev
            self.remove(lru)
            del self.cache[lru.key]
