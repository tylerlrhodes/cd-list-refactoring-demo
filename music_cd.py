""" MusicCD Item For Linked List """

class MusicCD:
    """ Music CD Item for Linked LIst """
    def __init__(self, artist, title, year, cdid):
        self.artist = artist
        self.title = title
        self.year = year
        self.cdid = cdid

    def __str__(self):
        return f"__str__:{self.title} by {self.artist} from {self.year}"

    def comparator(self, other):
        """ Comparator function for sorting """
        if self.title.lower() == other.title.lower():
            return 0
        if self.title.lower() > other.title.lower():
            return 1
        return -1

    def display(self):
        """ Display Music Item """
        return f"{self.title} by {self.artist} from {self.year}"
        