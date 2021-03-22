"""
=============
Mòdul Hashtag
=============
"""

class Hashtag(object):
    """
    
    Classe Hashtag

    >>> u = Hashtag("muntanya")
    >>> u2 = Hashtag("montanya")
    >>> print(u)
    #muntanya

    >>> print(u2)
    #montanya
    """

    def __init__(self, id):
        """

        >>> u = Hashtag("muntanya")
        >>> u.id
        'muntanya'
        """
        self.id = id

    def __str__(self):
        """

        >>> u = Hashtag("muntanya")
        >>> print(u)
        #muntanya
        """
        return "#" + str(self.id)

    def __repr__(self):
        """

        >>> u = Hashtag("muntanya")
        >>> u.id
        'muntanya'
        """
        return str(self.id)


    def __eq__(self, other):
        """
        >>> u = Hashtag("muntanya")
        >>> u3 = Hashtag("muntanya")
        >>> u == u3
        True
        """
        return self.id==other.id
