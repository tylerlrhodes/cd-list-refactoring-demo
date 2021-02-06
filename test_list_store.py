""" ListStore Unit Tests """
import unittest
from list_store import ListStore
from linked_list import LinkedList

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

class TestListStore(unittest.TestCase):
    """ Linked List Unit Test Class """
    @staticmethod
    def test_construct():
        """ Basic Test to Construct ListStore """
        l = ListStore([1, 2, 3])
        assert len(l) == 3

    @staticmethod
    def test_sort():
        """ Test sorting capability """
        l = ListStore([3, 2, 7, 1])
        after = sorted(l)
        assert after[0] == 1
        ll = LinkedList(None)
        ll.add_to_list(Item("3"))
        ll.add_to_list(Item("2"))
        ll.add_to_list(Item("1"))
        store2 = ListStore(ll, sort_method=sorted,
                           key_selector=lambda n: n.item.title)
        store2 = store2.sort()
        assert store2[0].item.title == "1"
        assert isinstance(store2, list)


if __name__ == "__main__":
    unittest.main()
