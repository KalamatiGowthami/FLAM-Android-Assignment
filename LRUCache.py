class LRUCache:
    # node for dll
    class Node:
        def __init__(self, key=0, value=0):
            self.key = key
            self.value = value
            self.prev = None
            self.next = None
    
    def __init__(self, capacity):
        # initialie LRU cachw.
        self.capacity = capacity
        self.cache = {}  
        
        
        self.head = self.Node()  
        self.tail = self.Node()  
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _add_node(self, node):
        
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
    
    def _remove_node(self, node):
       
        prev = node.prev
        next_node = node.next
        prev.next = next_node
        next_node.prev = prev
    
    def _move_to_head(self, node):
        
        self._remove_node(node)
        self._add_node(node)
    
    def _pop_tail(self):
        
        node = self.tail.prev
        self._remove_node(node)
        return node
    
    def get(self, key):
        if key not in self.cache:
            return -1
        
        #update teh node most recently used.
        node = self.cache[key]
        self._move_to_head(node)
        return node.value
    
    def put(self, key, value):
       
        
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._move_to_head(node)
            return
        
      
        new_node = self.Node(key, value)
        self.cache[key] = new_node
        self._add_node(new_node)
        
       
        if len(self.cache) > self.capacity:
            lru_node = self._pop_tail()
            del self.cache[lru_node.key]


if __name__ == "__main__":
  
    print("-----------------------")
    
    
    cache = LRUCache(2)
    
 
    
    cache.put(1, 1)
    cache.put(2, 2)
    
    
    print(f"key 1: {cache.get(1)}")  
    
    
    
    cache.put(3, 3) 
    
    print(f"key 2: {cache.get(2)}")  
    
    cache.put(4, 4)  
    print(f"key 1: {cache.get(1)}")  
    print(f"key 3: {cache.get(3)}")  
    print(f"key 4: {cache.get(4)}")  
    
    