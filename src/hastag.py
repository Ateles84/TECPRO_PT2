"""
============
Mòdul Hastag
============
"""

class Hastag(object):
    """
    """

    def __init__(self, id):
        """
        """
        self.id = id

    def __str__(self):
        """
        """
        return "#"+self.id

    def __eq__(self, other):
        """
        """
        return self.id==other.id

if __name__=='__main__':
    u = Hastag("muntanya")
    u2 = Hastag("montanya")
    u3 = Hastag("muntanya")
    print(u)
    print(u2)
    print(u==u3)
