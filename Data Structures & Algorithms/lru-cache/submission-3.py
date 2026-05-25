class ListNode:
    def __init__(self,key=0,value=0,prev=None,next=None):
        self.key = key
        self.value = value
        self.prev= prev
        self.next = next


class LRUCache:

    def __init__(self, capacity: int):        
        self.size = capacity
        self.lru = {}
        self.left = ListNode()
        self.right = ListNode()

        self.left.next = self.right
        self.right.prev = self.left

    def insert(self,node):
        prev = self.right.prev
        nxt = self .right

        prev.next = node
        node.next = nxt
        nxt.prev = node
        node.prev = prev
        return
    def delete(self,node):
        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev
        return

    def get(self, key: int) -> int:
        if key in self.lru:
            node = self.lru[key]
            val = node.value
            self.delete(node)
            self.insert(node)
            return  val
        return -1


    def put(self, key: int, value: int) -> None:
        if key in self.lru:
            node = self.lru[key]
            self.delete(node)
        self.lru[key] = ListNode(key,value)
        node = self.lru[key]
        self.insert(node)
        print(self.lru)
        if len(self.lru) > self.size:
            nxt_node = self.left.next
            self.delete(nxt_node)
            del self.lru[nxt_node.key]

        return
        
