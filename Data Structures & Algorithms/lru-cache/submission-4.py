
class ListNode:

    def __init__(self,key = 0,val = 0,prev = None,next = None):
        self.prev = prev
        self.next = next
        self.key = key
        self.val = val


class LRUCache:

    def __init__(self, capacity: int):
        self.left = ListNode()
        self.right = ListNode()
        self.left.next = self.right
        self.right.prev = self.left
        self.map = {}
        self.size = capacity

    def insert(self, node) -> None:
        prev = self.right.prev
        nxt = self.right

        prev.next = node
        node.prev = prev

        node.next = nxt
        nxt.prev = node
        return 

    def remove(self,node):
        prv = node.prev
        nxt = node.next

        prv.next = nxt
        nxt.prev = prv

        # node.next = None
        # node.prev = None
        return


    def get(self, key: int) -> int:
        if key in self.map:
            node = self.map[key]
            self.remove(node)
            self.insert(node)
            
            return node.val

        return -1


    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            print(node)
            self.remove(node)
            
        node = ListNode(key,value)
        # self.right.prev = node
        self.map[key] = node
        self.insert(node)

        if len(self.map) > self.size:
            nxt_node = self.left.next
            self.remove(nxt_node)
            del self.map[nxt_node.key]
        return
        
