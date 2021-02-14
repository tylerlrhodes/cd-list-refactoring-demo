""" Linked List Implementation """

from collections.abc import MutableSequence

###CodeSnippet-linked_list_snippet1b###
class Node:
    """ Node class """
    def __init__(self, item):
        self.item = item
        self.next = None

    def compare(self, other):
        """ Compare self to other through item comparator """
        return self.item.comparator(other)


class LinkedList(MutableSequence):
    """ LinkedList Class """
    def __init__(self, node):
        self.head = node
        self._ptr = None

    def __delitem__(self, index):
        # set the previous item's next to the item at the index's next
        if index == 0:
            if self.head is None:
                raise Exception("No item to delete")
            self.head = self.head.next
            return
        prev = None
        cur = self.head
        i = 0
        while i < index and cur is not None:
            prev = cur
            cur = cur.next
            i += 1
        if i != index and cur is None:
            raise Exception("Index out of range")
        prev.next = cur.next

    def __setitem__(self, index, value):
        i = 0
        cur = self.head
        while i != index and cur is not None:
            cur = cur.next
            i += 1
        if cur is None or i != index:
            raise Exception("Invalid index")
        cur.item = value
        #self.seq.__setitem__(index, value)

    def insert(self, index, value):
        # set new nodes's next to prev.next
        # set prev.next to new node with value
        # needs error checking!  index 1 and head null will fail
        if index == 0:
            n = Node(value)
            n.next = self.head
            self.head = n
            return
        prev = None
        cur = self.head
        i = 0
        while cur is not None and i != index:
            prev = cur
            cur = cur.next
            i += 1
        n = Node(value)
        n.next = prev.next
        prev.next = n
        #self.seq.insert(index, value)

    def __getitem__(self, index):
        if isinstance(index, slice):
            return [self[ii] for ii in range(*index.indices(len(self)))]

        if index > len(self) - 1:
            # this appears to be required when sorted is called
            # on the LinkedList!
            raise IndexError
        i = 0
        cur = self.head
        while i != index and cur is not None:
            cur = cur.next
            i += 1
        if i != index:
            raise Exception("Error on index")
        if cur is not None:
            return cur.item
        return None

    def __len__(self):
        """ Return count """
        i = 0
        p = self.head
        while p is not None:
            i += 1
            p = p.next
        return i

    def __iter__(self):
        self._ptr = self.head
        return self

    def __next__(self):
        n = self._ptr
        if self._ptr is None:
            raise StopIteration
        self._ptr = self._ptr.next
        return n

    def get_last_node(self):
        """ Gets the last node """
        ln = self.head
        while ln is not None and ln.next is not None:
            ln = ln.next
        return ln

    def add_to_list(self, item):
        """ Adds item to list """
        n = Node(item)
        ln = self.get_last_node()
        if ln is None:
            self.head = n
        else:
            ln.next = n

    def sort(self):
        """ Sorts list using bubble sort algorithm """
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
        """ Reverse the list """
        p = None
        current = self.head
        while current is not None:
            nxt = current.next
            if nxt is not None:
                self.head = nxt
            current.next = p
            p = current
            current = nxt

    def reverse_recur(self, p=None, current=None):
        """ Reverse the list recursively """
        if p is None:
            current = self.head
        if current is not None:
            nxt = current.next
            if nxt is not None:
                self.head = nxt
            current.next = p
            self.reverse_recur(current, nxt)

    def delete(self, item):
        """ Delete an item """
        n, prev = self.find_node(item)
        if prev is None:
            self.head = n.next
        else:
            prev.next = n.next

    def insert_after(self, item_to_insert, item_after):
        """ insert before item """
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

    # def __len__(self):
    #     return self.count()

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

    def find_node(self, item):
        """ Finds a node """
        prev = None
        for n in self:
            if n.compare(item) == 0:
                return n, prev
            prev = n
        return None

    def merge(self, other):
        """ merge the two lists  """
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
                    a = a.next
            else:
                while b is not None:
                    new_list.add_to_list(b.item)
                    b = b.next
        self.head = new_list.head

###CodeSnippetEnd-linked_list_snippet1b###
