class ListNode:
    def __init__(self,key = 0,val = 0,prev = None,next = None) -> None:
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev
class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.left = ListNode()
        self.right = ListNode()
        self.left.next = self.right
        self.right.prev = self.left
        self.hmap = {}

    def get(self, key: int) -> int:
        if key in self.hmap:

            self.remove(self.hmap[key])
            self.insert(self.hmap[key])

            return self.hmap[key].val
        return -1
        
    def insert(self,node):
        prev = self.right.prev
        nxt = self.right

        prev.next= node
        node.prev = prev
        node.next = nxt
        nxt.prev = node
    def remove(self,node):
        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev

    def put(self, key: int, value: int) -> None:
        if key not in self.hmap:
            val = ListNode(key,value)
            self.insert(val)
            self.hmap[key] =val
        if len(self.hmap) > self.size:
            lru = self.left.next
            self.remove(lru)
            del self.hmap[lru.key]
        self.remove(self.hmap[key])
        node = ListNode(key, value)
        self.insert(node)
        self.hmap[key] = node
        
