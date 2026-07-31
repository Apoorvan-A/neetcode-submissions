class Node:
    def __init__ (self,key,val):
        self.key=key
        self.val=val
        self.prev=None
        self.next=None


class LRUCache:
    def __init__(self, capacity: int):
        self.cap=capacity
        self.cache={}
        self.head,self.tail=Node(-1,-1),Node(-1,-1)
        self.head.next=self.tail
        self.tail.prev=self.head

    def remove(self,node):
        node.prev.next=node.next
        node.next.prev=node.prev

    def insert(self,node):
        node.next=self.head.next
        self.head.next.prev=node
        self.head.next=node
        node.prev=self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            node=self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node=self.cache[key]
            node.val=value
            self.remove(node)
            self.insert(node)
        else:
            node=Node(key,value)
            self.cache[key]=node
            if len(self.cache)>self.cap:
                lru = self.tail.prev
                self.remove(lru)
                self.cache.pop(lru.key)
            self.insert(node)

