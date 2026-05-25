
class ListNode:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    #11.33

    def __init__(self, capacity: int):
        self.left,self.right = ListNode(0,0), ListNode(0,0)
        self.left.next = self.right
        self.right.prev = self.left
        self.cap =capacity
        self.hashMap = {}
        
    def insert(self,node):
        prev = self.right.prev
        nxt = self.right
        prev.next = node
        node.prev =prev
        node.next = nxt
        self.right.prev =node
    
    def delete(self,node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def get(self, key: int) -> int:
        if key in self.hashMap:
            self.delete(self.hashMap[key])
            self.insert(self.hashMap[key])
            return self.hashMap[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:

        if key in self.hashMap:
            self.delete(self.hashMap[key])
        self.hashMap[key] = ListNode(key,value)
        self.insert(self.hashMap[key])
        if len(self.hashMap) > self.cap:
            lru = self.left.next
            self.delete(lru)
            del self.hashMap[lru.key]
        

        
