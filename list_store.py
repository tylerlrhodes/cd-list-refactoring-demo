""" List Store Class """

from collections.abc import MutableSequence
from wrapt import synchronized


class ListStore(MutableSequence):
    """ List Store """

    def __init__(self, seq=None,
                 sort_method=sorted, key_selector=lambda x: x,
                 reverse=False):
        self.seq = seq
        self.sort_method = sort_method
        self.key_selector = key_selector
        self.reverse = reverse

    def sort(self):
        """ Sorts the sequence """
        return self.sort_method(self.seq, key=self.key_selector, reverse=self.reverse)

    def __delitem__(self, index):
        self.seq.__delitem__(index)

    def __setitem__(self, index, value):
        self.seq.__setitem__(index, value)

    def insert(self, index, value):
        self.seq.insert(index, value)

    def __getitem__(self, index):
        return self.seq.__getitem__(index)

    def __len__(self):
        return len(self.seq)


class ThreadSafeListStore(ListStore):
    """ Thread Safe List Store """

    @synchronized
    def __init__(self, seq=None,
                 sort_method=sorted, key_selector=lambda x: x,
                 reverse=False):
        super().__init__(seq, sort_method, key_selector, reverse)

    @synchronized
    def sort(self):
        """ Sorts the sequence """
        return self.sort_method(self.seq, key=self.key_selector, reverse=self.reverse)

    @synchronized
    def __delitem__(self, index):
        self.seq.__delitem__(index)

    @synchronized
    def __setitem__(self, index, value):
        self.seq.__setitem__(index, value)

    @synchronized
    def insert(self, index, value):
        self.seq.insert(index, value)

    @synchronized
    def __getitem__(self, index):
        return self.seq.__getitem__(index)

    @synchronized
    def __len__(self):
        return len(self.seq)
