"""
============
Mòdul Hashtag
============
"""

class Hashtag(object):
    """
    """

    def __init__(self, id):
        """
        """
        self.id = id

    def __str__(self):
        """
        """
        return "#" + str(self.id)

    def __repr__(self):
        return str(self.id)


    def __eq__(self, other):
        """
        """
        return self.id==other.id

if __name__=='__main__':
    u = Hashtag("muntanya")
    u2 = Hashtag("montanya")
    u3 = Hashtag("muntanya")
    print(u)
    print(u2)
    print(u==u3)
