"""
Unit Tests for Linked List
"""
###CodeSnippet-test_linked_list_snippet1a###
import unittest
from linked_list import LinkedList, Node

class Item:
    """ Default Item for Linked List Test """
    def __init__(self, title):
        self.title = title

    def comparator(self, other):
        """ Comparator for item """
        if self.title.lower() == other.title.lower():
            return 0
        if self.title.lower() > other.title.lower():
            return 1
        return -1

class TestLinkedList(unittest.TestCase):
    """ Linked List Unit Test Class """
    @staticmethod
    def _validate_list(linked_list, items = None):
        for idx, val in enumerate(linked_list):
            assert items[idx].title == val.item.title

    @staticmethod
    def _gen_tmp_list():
        tmp = LinkedList(None)
        item_1 = Item("a")
        item_2 = Item("b")
        item_3 = Item("c")
        tmp.add_to_list(item_1)
        tmp.add_to_list(item_2)
        tmp.add_to_list(item_3)
        return tmp, [item_1, item_2, item_3]

    @staticmethod
    def test_iterator():
        """ Test the iterator """
        a, b, c = Item("a"), Item("b"), Item("c")
        tmp = LinkedList(Node(a))
        tmp.head.next = Node(b)
        tmp.head.next.next = Node(c)
        TestLinkedList._validate_list(tmp, [a, b, c])
        assert len(tmp) == 3, "Expected 3"

    @staticmethod
    def test_get_last_node():
        """ Test getting the last node """
        a,b,c = Item("a"), Item("b"), Item("c")
        tmp = LinkedList(None)
        tmp.add_to_list(a)
        assert tmp.get_last_node().item is a, "Expected last to be Item a"
        tmp.add_to_list(b)
        tmp.add_to_list(c)
        assert tmp.get_last_node().item is c, "Expected last to be Item c"

    @staticmethod
    def test_sort():
        """ Test sorting the linked list """
        tmp, [i1, i2, i3] = TestLinkedList._gen_tmp_list()
        tmp.sort()
        TestLinkedList._validate_list(tmp, [i1, i2, i3])
        i4 = Item("d")
        i5 = Item("e")
        i6 = Item("f")
        tmp.add_to_list(i5)
        tmp.add_to_list(i6)
        tmp.add_to_list(i4)
        tmp.sort()
        TestLinkedList._validate_list(tmp, [i1, i2, i3, i4, i5, i6])
        tmp2 = LinkedList(None)
        tmp2.add_to_list(i1)
        tmp2.sort()
        TestLinkedList._validate_list(tmp2, [i1])

    @staticmethod
    def test_reverse():
        """ Test reversing the linked list"""
        item_d = Item("d")
        tmp = LinkedList(None)
        tmp.add_to_list(item_d)
        tmp.reverse()
        TestLinkedList._validate_list(tmp, [item_d])
        tmp, [i1, i2, i3] = TestLinkedList._gen_tmp_list()
        tmp.add_to_list(item_d)
        tmp.reverse()
        TestLinkedList._validate_list(tmp, [item_d, i3, i2, i1])

    @staticmethod
    def test_reverse_recur():
        """ Test recursively reversing the linked list """
        item_d = Item("d")
        tmp = LinkedList(None)
        tmp.add_to_list(item_d)
        tmp.reverse_recur()
        TestLinkedList._validate_list(tmp, [item_d])
        tmp, [i1, i2, i3] = TestLinkedList._gen_tmp_list()
        tmp.add_to_list(item_d)
        tmp.reverse_recur()
        TestLinkedList._validate_list(tmp, [item_d, i3, i2, i1])

    @staticmethod
    def test_insert():
        """ Test inserting an item into the linked list (MutableSequence) """
        ## This tests a MutableSequene Override
        tmp, [i1, i2, i3] = TestLinkedList._gen_tmp_list()
        i4 = Item("d")
        tmp.insert(3, i4)
        TestLinkedList._validate_list(tmp, [i1, i2, i3, i4])
        i5 = Item("e")
        tmp.insert(0, i5)
        TestLinkedList._validate_list(tmp, [i5, i1, i2, i3, i4])
        i6 = Item("f")
        tmp.insert(2, i6)
        TestLinkedList._validate_list(tmp, [i5, i1, i6, i2, i3, i4])

    @staticmethod
    def test_del_item():
        """ Test MutableSequence del item """
        tmp, [_, i2, _] = TestLinkedList._gen_tmp_list()
        del tmp[0]
        assert len(tmp) == 2
        i4 = Item("d")
        tmp.insert(len(tmp), i4)
        del tmp[1]
        assert len(tmp) == 2
        tmp.insert(len(tmp), Item("e"))
        del tmp[2]
        assert len(tmp) == 2
        TestLinkedList._validate_list(tmp, [i2, i4])
        tmp.remove(i2)
        TestLinkedList._validate_list(tmp, [i4])

    @staticmethod
    def test_get_item():
        """ Test MutableSequence __getitem__ """
        tmp, [i1, i2, i3] = TestLinkedList._gen_tmp_list()
        assert i1.title == tmp[0].title
        assert i2.title == tmp[1].title
        assert i3.title == tmp[2].title
        TestLinkedList._validate_list(tmp, [i1, i2, i3])

    @staticmethod
    def test_set_item():
        """ Test MutableSequence __getitem__ """
        tmp, [i1, i2, i3] = TestLinkedList._gen_tmp_list()
        tmp[0].title = "z"
        tmp[1].title = "l"
        tmp[2].title = "q"
        assert tmp[0].title == "z"
        assert tmp[1].title == "l"
        assert tmp[2].title == "q"
        TestLinkedList._validate_list(tmp, [i1, i2, i3])
    # count is not the best method to have here
    # @staticmethod
    # def test_count():
    #     """ Test getting a count of items """
    #     tmp, items = TestLinkedList._gen_tmp_list()
    #     assert tmp.count() == len(items), "Expected equal lengths"
    #     assert len(tmp) == len(items), "Expected equal lengths"

    @staticmethod
    def test_merge():
        """ Test mergint the linked list """
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
        TestLinkedList._validate_list(l1, items)

    @staticmethod
    def test_add():
        """ Test adding an item to the linked list """
        tmp = LinkedList(None)
        tmp.add_to_list(Item("a"))
        assert len(tmp) == 1
        tmp.add_to_list(Item("b"))
        tmp.add_to_list(Item("c"))
        assert len(tmp) == 3
        titles_correct = ["a", "b", "c"]
        for idx, val in enumerate(tmp):
            assert titles_correct[idx] == val.item.title

    @staticmethod
    def test_delete():
        """ Test deleting an item from the linked list """
        tmp, items = TestLinkedList._gen_tmp_list()
        tmp.delete(items[2])
        items.remove(items[2])
        TestLinkedList._validate_list(tmp, items)
        tmp, [i1, i2, i3] = TestLinkedList._gen_tmp_list()
        tmp.delete(i2)
        TestLinkedList._validate_list(tmp, [i1, i3])
        tmp, [i1, i2, i3] = TestLinkedList._gen_tmp_list()
        tmp.delete(i1)
        TestLinkedList._validate_list(tmp, [i2, i3])

if __name__ == "__main__":
    unittest.main()
###CodeSnippetEnd-test_linked_list_snippet1a###
