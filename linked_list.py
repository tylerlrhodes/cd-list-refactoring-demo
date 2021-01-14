
# __str__

# Standard Linked List
### Interface for display
### Interface for sort
### Interface for search

#### Sort a linked list in place

### Linked List Uses
### Constant time insertion
### Priority Queue - insert into middle
### Queue


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

def print_music_list(music_list):
    for cd in music_list:
        print(f"CD: {cd.item}")

if __name__ == "__main__":

    music_list = LinkedList(None)

    kid_a = MusicCD("Radiohead", "Kid A", 2000, 1)
    the_bends = MusicCD("Radiohead", "The Bends", 1995, 2)
    the_king_of_limbs = MusicCD("Radiohead", "The King of Limbs - Live from the Basement", 2011, 3)
    crash = MusicCD("Dave Matthews Band", "Crash", 1996, 4)
    american_idiot = MusicCD("Green Day", "American Idiot", 2004, 5)
    vsq_strung_out_vol9 = MusicCD("Vitamin String Quartet", "Strung Out, Vol. 9: VSQ Performs Music's Biggest Hits", 2008, 6)

    music_list.add_to_list(kid_a)
    music_list.add_to_list(the_bends)
    music_list.add_to_list(the_king_of_limbs)
    music_list.add_to_list(crash)
    music_list.add_to_list(american_idiot)
    music_list.add_to_list(vsq_strung_out_vol9)

    print(f"Count of list: {len(music_list)}")

    print_music_list(music_list)

    music_list.sort()

    print(f"\n#\n#\n#\nPost Sort:\n")

    print_music_list(music_list)

    music_list.delete(the_bends)

    print(f"Delete the_bends")

    print_music_list(music_list)

    music_list.delete(american_idiot)

    print(f"Delete american_idiot")

    print_music_list(music_list)
    
    
    music_list.insert(american_idiot, crash)

    print(f"Inserted america_idiot before crash...")

    print_music_list(music_list)
    
    print(f"Inserted the_bends before vsq_strung_out...")

    music_list.insert(the_bends, vsq_strung_out_vol9)

    print_music_list(music_list)

    music_list.sort()

    print(f"Sort it again....")

    print_music_list(music_list)


    # music_list.reverse()

    # print_music_list(music_list)

    # music_list.reverse_recur()

    # print_music_list(music_list)













# Test 1 item in list
# Test Empty list
# Test 2 item list
# test 10 items list












# Double Linked List


# LISP Style : CAR CDR 
