class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}
        self.left = self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left
    
    def insert(self, node):
        prevNode = self.right.prev
        nextNode = self.right

        prevNode.next = node
        node.prev = prevNode

        node.next = nextNode
        nextNode.prev = node

    def remove(self, node):
        prevNode = node.prev
        nextNode = node.next

        prevNode.next = nextNode
        nextNode.prev = prevNode

    def get(self, key: int) -> int:
        if key in self.hashmap:
            self.remove(self.hashmap[key])
            self.insert(self.hashmap[key])
            return self.hashmap[key].val
        return -1

        

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.remove(self.hashmap[key])
        self.hashmap[key] = Node(key, value)
        self.insert(self.hashmap[key])
        
        if len(self.hashmap) > self.capacity:
            LRU = self.left.next
            self.remove(LRU)
            del self.hashmap[LRU.key]

        
