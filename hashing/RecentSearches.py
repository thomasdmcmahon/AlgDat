"""Effectively Store and Preview the last n (string) searches done by user"""

class Node:
    """Doublelinked node representing a search"""
    def __init__(self, key):
        self.key = key
        self.next = None
        self.prev = None

class RecentSearches:
    """Keep track over the last searches with O(1) lookup and update"""
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {} # Key -> Node
        self.head = None # latest search
        self.tail = None
    
    def _add_to_front(self, node: Node):
        """Add node to the front of list (latest search)"""
        node.prev = None
        node.next = self.head
        if self.head:
            self.head.prev = node
        self.head = node
        if not self.tail: # first elem
            self.tail = node
    
    def _remove_node(self, node: Node):
        """Remove a node from the link"""
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next # node was head
        
        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev
        
        node.prev = node.next = None
    
    def _move_to_front(self, node: Node):
        """Move existing node to front of list (latest search)"""
        self._remove_node(node)
        self._add_to_front(node)
    
    def update(self, key: str):
        """
        Update the search with 'key'.
        If key exists -> move node to front.
        If not -> create new node, add to front,
        remove current head and shift if capacity is exceeded
        """
        if key in self.map:
            node = self.map[key]
            self._move_to_front(node)
        else:
            new_node = Node(key)
            self.map[key] = new_node
            self._add_to_front(new_node)

            if len(self.map) > self.capacity:
                # Remove last node
                old_tail = self.tail
                self._remove_node(old_tail)
                del self.map[old_tail.key]
    
    def get_recent(self):
        """Returns a list over searches from latest to last."""
        results = []
        node = self.head
        while node:
            results.append(node.key)
            node = node.next
        return results
