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

    >>> print(u1.nick)
    <BLANKLINE>

    >>> print(u2.getHashtag()==u1.getHashtag())
    True
    """

    def __init__(self, contingut,id_hashtag):
        """
        Constructor

        >>> u = Posts("NestleJunly")
        >>> u.nick
        ''
        """
        global id
        self.id = id
        id += 1
        self.cont = contingut
        self.nick = ""
        self.hashtag = id_hashtag

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
        No realitzem docTest perque mai donara be
        """
        return self.__date

    def getId(self):
        """
        """
        return self.id

    def getHashtag(self):
        """
        """
        return Hashtag(self.hashtag)

    def __str__(self):
        """
        """
        return "Post id: " + str(self.id) + " | Usuari: " + str(self.nick) +" | info: "+ str(self.cont) + " | Hashtag: " + str(self.hashtag) + " | Date: #"+str(self.__date)

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
        >>> u.nick
        'bbp'
        """
        self.nick = nick

    def registraHashtag(self, id):
        """
        """
        self.hashtag = Hashtag(id)

if __name__ == '__main__':
    u = Posts("Bon dia!")
    u1 = Posts("Bona dia!")
    u2 = Posts("Bon dia!")
    print(u)
    print(u1)
    print(u2)
    print(u2.info())
    print(u==u1)
    print(u2.getHashtag()==u1.getHashtag())
