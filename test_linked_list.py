

import unittest
from linked_list import LinkedList, MusicCD

class Item:
    def __init__(self, title):
        self.title = title 
    
    def comparator(self, other):
        if self.title.lower() == other.title.lower():
            return 0
        elif self.title.lower() > other.title.lower():
            return 1
        else:
            return -1

class TestLinkedList(unittest.TestCase):
    
    def _validate_list(self, linked_list, cds = []):
        for idx, val in enumerate(linked_list):
            assert cds[idx].title == val.item.title

    def test_add(self):
        tmp = LinkedList(None)
        tmp.add_to_list(Item("a"))
        assert tmp.count() == 1
        tmp.add_to_list(Item("b"))
        tmp.add_to_list(Item("c"))
        assert tmp.count() == 3
        # iterate and check order of items
        titles_correct = ["a", "b", "c"]
        for idx, val in enumerate(tmp):
            assert titles_correct[idx] == val.item.title 

    def test_delete(self):
        # check delete from end
        # check delete from middle
        # check delete from head
        def gen_tmp_items():
            #use randomly numbered titles
            #option for a configured number of items to generate
            tmp = LinkedList(None)
            i1 = Item("a")
            i2 = Item("b")
            i3 = Item("c")
            tmp.add_to_list(i1)
            tmp.add_to_list(i2)
            tmp.add_to_list(i3)
            return tmp, [i1, i2, i3]
        tmp, items = gen_tmp_items()
        tmp.delete(items[2])
        items.remove(items[2])
        self._validate_list(tmp, items)

if __name__ == "__main__":
    # Test add
    unittest.main()