

###CodeSnippet-linked_list_snippet1b###

import unittest

class MusicCD:
    def __init__(self, artist, title, year, cdid):
        self.artist = artist
        self.title = title 
        self.year = year
        self.cdid = cdid
    
    def __str__(self):
        return f"__str__:{self.title} by {self.artist} from {self.year}"

    def comparator(self, other):
        if self.title.lower() == other.title.lower():
            return 0
        elif self.title.lower() > other.title.lower():
            return 1
        else:
            return -1

    def display(self):
        return f"{self.title} by {self.artist} from {self.year}"

class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

    def compare(self, other):
        return self.item.comparator(other)

class LinkedList:
    def __init__(self, node):
        self.head = node

    def __iter__(self):
        self._ptr = self.head
        return self
    
    def __next__(self):
        n = self._ptr
        if self._ptr == None:
            raise StopIteration
        else:
            self._ptr = self._ptr.next
            return n

    def get_last_node(self):
        ln = self.head
        while ln != None and ln.next != None:
            ln = ln.next
        return ln

    def add_to_list(self, item):
        n = Node(item)
        ln = self.get_last_node()
        if ln == None:
            self.head = n
        else:
            ln.next = n

    def sort(self):
        # bubble sort it
        start = True 
        while start:
            prev = None
            start = False 
            for n in self:
                a = n 
                b = n.next 
                if b is not None and a.compare(b.item) == 1:
                    self.__swap(prev, a, b)
                    start = True
                prev = a 
        return 

    def reverse(self):
        p = None
        current = self.head 
        while current != None:
            next = current.next
            if next != None: 
                self.head = next
            current.next = p 
            p = current
            current = next 
        return
    
    def reverse_recur(self, p=None, current=None):
        if p == None:
            current = self.head
        if current != None:
            next = current.next 
            if next != None:
                self.head = next
            current.next = p
            self.reverse_recur(current, next)
        return

    def delete(self, item):
        n, prev = self.find_node(item)
        if prev is None:
            self.head = n.next 
        else:
            prev.next = n.next
        return 
    
    def insert(self, item_to_insert, item_after):
        #insert before item
        n, prev = self.find_node(item_after)
        if n is None:
            raise ValueError("Error finding item to insert before...")
        # if prev is null, then item_after is head, insert before
        if prev is None:
            node = Node(item_to_insert)
            node.next = self.head
            self.head = node
        #else, insert between prev and n 
        else:
            node = Node(item_to_insert)
            prev.next = node 
            node.next = n 

    def __len__(self):
        return self.count()

    def __swap(self, prev, a , b):
        self.__swap_adjacent(prev, a, b)

    def __swap_adjacent(self, prev, a, b):
        # swap nodes a and b, assuming previous is provided
        if a is None or b is None:
            raise ValueError("No value is provided for either node!")        
        a.next = b.next 
        b.next = a 
        if prev is not None:
            prev.next = b
        else:
            self.head = b  

    def count(self):
        i = 0
        p = self.head
        while p != None:
            i += 1
            p = p.next

        return i

    def find_node(self, item):
        prev = None 
        for n in self:  
            if n.compare(item) == 0:
                return n, prev 
            prev = n  
        return None
    
    def merge(self, other):
        # merge the two lists
        new_list = LinkedList(None)
        a = self.head
        b = other.head 
        while a is not None or b is not None:
            if a is not None and b is not None:
                if a.compare(b.item) <= 0:
                    new_list.add_to_list(a.item)
                    a = a.next 
                else:
                    new_list.add_to_list(b.item)
                    b = b.next 
            elif a is not None:
                while a is not None:
                    new_list.add_to_list(a.item)
                    a = a .next 
            else:
                while b is not None:
                    new_list.add_to_list(b.item)
                    b = b.next        
        self.head = new_list.head

###CodeSnippetEnd-linked_list_snippet1b###
