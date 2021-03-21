"""
==================
Mòdul Xarxa Social
==================
"""
from usuari import Usuari
from posts import Posts
from hastag import Hastag

class XarxaSocial(object):
    """
    """
    def __init__(self):
        self.__usuaris = {}
        self.__posts = {}
        self.__hastags = {}

    def afegeixUsuari(self,nick, email, password):
        """
        """
        if nick in self.__usuaris.keys():
            return "Usuari ja existent"
        else:
            u = Usuari(nick, email, password)
            self.__usuaris[nick] = []


    def afegeixHastag(self, id):
        """
        """
        if id in self.__hastags.keys():
            return "Hastag ja existent"
        else:
            h = Hastag(id)
            self.__hastags[id] = h

    def publicarPost(self, nick, id_hastag, contingut_post):
        """
        """
        if nick not in self.__usuaris:
            return "Usuari no creat"
        else:
            p = Posts(contingut_post, nick, id_hastag)
            self.__usuaris[nick] = p
            self.__posts[contingut_post] = p
    def users(self):
        """
        """
        return self.__usuaris.keys()

    def posts(self):
        """
        """
        return self.__posts.keys()
    def llistarPostsUser(self, nick):
        """
        """
        if nick not in self.__usuaris:
            return "Usuari no existeix"

        else:
            return self.__usuaris.get(nick)


if __name__=='__main__':
    i = XarxaSocial()
    i.afegeixUsuari('Bernat', 'b@gmail.com', 'bbrunet')
    i.afegeixHastag("muntanya")
    i.publicarPost("pere","muntanya","into the wild")
    i.publicarPost("Bernat","muntanya","into the wild")
    i.publicarPost("Bernat","muntnya","into th wild")
    print(i.users())
    print(i.posts())
    print(i.llistarPostsUser("Bernat"))
