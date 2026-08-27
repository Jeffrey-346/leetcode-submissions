class LRUCache:
    # doubly linked list
    class ListNode:
        def __init__(self, val=0, prev=None, next=None):
            self.val = val
            self.prev = prev
            self.next = next

    def __init__(self, capacity: int):
        self.used = 0
        self.capacity = capacity
        self.cache = self.ListNode()
        self.tail = self.cache
        self.m = {} # map key to node

        

    def get(self, key: int) -> int:
        if key in self.m:
            node = self.m[key]
            if node == self.tail:
                return self.m[key].val[1]
            # update LRU
            # remove from ll
            node.prev.next = node.next
            node.next.prev = node.prev

            # add to end
            node.next = None
            node.prev = self.tail
            self.tail.next = node
            self.tail = self.tail.next

            return self.m[key].val[1]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # if node is already in Cache
        if key in self.m:
            # update LRU
            node = self.m[key]
            if node == self.tail:
                node.val[1] = value
                return

            node.prev.next = node.next
            node.next.prev = node.prev

            node.next = None
            node.prev = self.tail
            self.tail.next = node
            self.tail = self.tail.next

            node.val[1] = value
            return

        if self.used == self.capacity:
            victim = self.cache.next
            # remove from front of ll
            self.cache.next = victim.next
            if victim.next:
                victim.next.prev = self.cache
            del self.m[victim.val[0]]
            self.used -= 1
        # add new node
        new_node = self.ListNode([key, value], prev=self.tail) 
        self.m[key] = new_node
        self.tail.next = new_node
        self.tail = self.tail.next
        self.used += 1

        
