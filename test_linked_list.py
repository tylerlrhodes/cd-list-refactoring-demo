

###CodeSnippet-linked_list_snippet1b###
import unittest
from linked_list import LinkedList, Node

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
    
    def _validate_list(self, linked_list, items = []):
        for idx, val in enumerate(linked_list):
            assert items[idx].title == val.item.title

    def _gen_tmp_list(self):
        tmp = LinkedList(None)
        i1 = Item("a")
        i2 = Item("b")
        i3 = Item("c")
        tmp.add_to_list(i1)
        tmp.add_to_list(i2)
        tmp.add_to_list(i3)
        return tmp, [i1, i2, i3]

    def test_iterator(self):
        a, b, c = Item("a"), Item("b"), Item("c")
        tmp = LinkedList(Node(a))
        tmp.head.next = Node(b)
        tmp.head.next.next = Node(c)
        self._validate_list(tmp, [a, b, c])
        assert len(tmp) == 3, "Expected 3"

    def test_get_last_node(self):
        a,b,c = Item("a"), Item("b"), Item("c")
        tmp = LinkedList(None)
        tmp.add_to_list(a)
        assert tmp.get_last_node().item is a, "Expected last to be Item a"
        tmp.add_to_list(b)
        tmp.add_to_list(c)
        assert tmp.get_last_node().item is c, "Expected last to be Item c"

    def test_sort(self):
        tmp, [i1, i2, i3] = self._gen_tmp_list()
        tmp.sort()
        self._validate_list(tmp, [i1, i2, i3])
        i4 = Item("d")
        i5 = Item("e")
        i6 = Item("f")
        tmp.add_to_list(i5)
        tmp.add_to_list(i6)
        tmp.add_to_list(i4)
        tmp.sort()
        self._validate_list(tmp, [i1, i2, i3, i4, i5, i6])
        tmp2 = LinkedList(None)
        tmp2.add_to_list(i1)
        tmp2.sort()
        self._validate_list(tmp2, [i1])

    def test_reverse(self):
        item_d = Item("d")
        tmp = LinkedList(None)
        tmp.add_to_list(item_d)
        tmp.reverse()
        self._validate_list(tmp, [item_d])
        tmp, [i1, i2, i3] = self._gen_tmp_list()
        tmp.add_to_list(item_d)
        tmp.reverse()
        self._validate_list(tmp, [item_d, i3, i2, i1])

    def test_reverse_recur(self):
        item_d = Item("d")
        tmp = LinkedList(None)
        tmp.add_to_list(item_d)
        tmp.reverse_recur()
        self._validate_list(tmp, [item_d])
        tmp, [i1, i2, i3] = self._gen_tmp_list()
        tmp.add_to_list(item_d)
        tmp.reverse_recur()
        self._validate_list(tmp, [item_d, i3, i2, i1])

    def test_insert(self):
        tmp, [i1, i2, i3] = self._gen_tmp_list()
        i4 = Item("d")
        tmp.insert(i4, i2)
        self._validate_list(tmp, [i1, i4, i2, i3])
        i5 = Item("e")
        tmp.insert(i5, i1)
        self._validate_list(tmp, [i5, i1, i4, i2, i3])

    def test_count(self):
        tmp, items = self._gen_tmp_list()
        assert tmp.count() == len(items), "Expected equal lengths"
        assert len(tmp) == len(items), "Expected equal lengths"

    def test_merge(self):
        letters = ["a", "c", "e", "g"]
        letters2 = ["b", "d", "f", "h"]
        items = []
        l1, l2 = LinkedList(None), LinkedList(None)
        for _, (i, i2) in enumerate(zip(letters, letters2)):
            l1.add_to_list(Item(i))
            items.append(Item(i))
            l2.add_to_list(Item(i2))
            items.append(Item(i2))
        l1.merge(l2)
        self._validate_list(l1, items)

        
    def test_add(self):
        tmp = LinkedList(None)
        tmp.add_to_list(Item("a"))
        assert tmp.count() == 1
        tmp.add_to_list(Item("b"))
        tmp.add_to_list(Item("c"))
        assert tmp.count() == 3
        titles_correct = ["a", "b", "c"]
        for idx, val in enumerate(tmp):
            assert titles_correct[idx] == val.item.title 

    def test_delete(self):
        tmp, items = self._gen_tmp_list()
        tmp.delete(items[2])
        items.remove(items[2])
        self._validate_list(tmp, items)
        tmp, [i1, i2, i3] = self._gen_tmp_list()
        tmp.delete(i2)
        self._validate_list(tmp, [i1, i3])
        tmp, [i1, i2, i3] = self._gen_tmp_list()
        tmp.delete(i1)
        self._validate_list(tmp, [i2, i3])

if __name__ == "__main__":
    unittest.main()
###CodeSnippetEnd-linked_list_snippet1b###