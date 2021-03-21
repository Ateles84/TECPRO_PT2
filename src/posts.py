"""
===========
Mòdul Posts
===========
"""
from hastag import Hastag
from datetime import datetime

id = 1

class Posts(object):
    """
    """

    def __init__(self, contingut, nick, hastag):
        """
        Constructor

        >>> u = Posts()
        >>> u.nick
        ''
        """
        global id
        self.id = id
        id = id +1
        self.cont = contingut
        self.nick = nick
        self.hastag = hastag
        datetim=datetime.now()
        self.__date=datetim.strftime("%c")

    def info(self):
        """
        """
        return self.cont

    def getDate(self):
        """
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

    def getHastag(self):
        """
        """
        return Hastag(self.hastag)

    def getContent(self):
        """
        """
        return self.cont

    def __str__(self):
        """
        """
        return "Post id: "+str(self.id)+" info: "+self.cont+ " Hashtag: " + self.hastag + " Date: "+str(self.__date)

    def __eq__(self, other):
        """
        """
        return self.cont==other.cont

    def __repr__(self):
        return "Post id: "+str(self.id)+" info: "+self.cont+ " Hashtag: " + self.hastag + " Date: "+str(self.__date)


if __name__=='__main__':
    u = Posts("Bon dia!","rebbant","noudia")
    u1 = Posts("Bona dia!","brenat","noudia")
    u2 = Posts("Bon dia!","brunet","noumati")
    print(u)
    print(u1)
    print(u2)
    print(u2.info())
    print(u==u1)
    print(u1.getNick())
    print(u2.getHastag()==u1.getHastag())
