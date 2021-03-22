"""
===========
Mòdul Posts
===========
"""
from hashtag import Hashtag
from datetime import datetime

id = 1

class Posts(object):
    """
    
    Classe Posts

    >>> u = Posts("Bon dia!")
    >>> u1 = Posts("Bona dia!")
    >>> u2 = Posts("Bon dia!")
    >>> print(u)
    Post id: 1 | Usuari:  | info: Bon dia! | Hashtag: [] | Date: Mon Mar 22 21:39:40 2021

    >>> print(u2.info())
    Bon dia!

    >>> print(u==u1)
    False

    >>> print(u1.getNick())
    ""

    >>> print(u2.getHashtag()==u1.getHashtag())
    True
    """

    def __init__(self, contingut):
        """
        Constructor

        >>> u = Posts()
        >>> u.nick
        ''
        """
        global id
        self.id = id
        id += 1
        self.cont = contingut
        self.nick = ""
        self.hashtag = []

        datetim=datetime.now()
        self.__date=datetim.strftime("%c")

    def info(self):
        """

        >>> u = Posts("Bon dia!")
        >>> u.info()
        'Bon dia!'
        """
        return self.cont

    def getDate(self):
        """

        >>> u = Posts("Bon dia!")
        >>> u.getDate()
        'Mon Mar 22 21:45:21 2021'
        """
        return self.__date

    def getId(self):
        """
        """
        return self.id

    def getNick(self):
        """

        """
        return self.nick

    def getHashtag(self):
        """
        """
        return Hashtag(self.hashtag)

    def __str__(self):
        """
        """
        return "Post id: " + str(self.id) + " | Usuari: " + str(self.nick) +" | info: "+ str(self.cont) + " | Hashtag: " + str(self.hashtag) + " | Date: "+str(self.__date)

    def __eq__(self, other):
        """
        """
        return self.cont==other.cont

    def __repr__(self):
        """
        """
        return "Post id: " + str(self.id) + " | Usuari: " + str(self.nick) +" | info: "+ str(self.cont) + " | Hashtag: " + str(self.hashtag) + " | Date: "+str(self.__date)

    def registraUsuari(self, nick):
        """

        >>> u = Posts("Bon dia!")
        >>> u.registraUsuari("bbp")
        >>> u.getNick()
        'bbp'
        """
        self.nick = nick

    def registraHashtag(self, id):
        """
        """
        self.hashtag.append(Hashtag(id))

if __name__ == '__main__':
    u = Posts("Bon dia!")
    u1 = Posts("Bona dia!")
    u2 = Posts("Bon dia!")
    print(u)
    print(u1)
    print(u2)
    print(u2.info())
    print(u==u1)
    print(u1.getNick())
    print(u2.getHashtag()==u1.getHashtag())
