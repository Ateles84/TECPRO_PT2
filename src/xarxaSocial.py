"""
==================
Mòdul Xarxa Social
==================
"""
from usuari import Usuari
from posts import Posts
from hastag import Hastag

class iTicApp(object):
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
        if nick not in list(self.__usuaris):
            print("Usuari no creat")
        else:
            p = Posts(contingut_post, nick, id_hastag)
            self.__usuaris[nick].append(p)

            if (nick not in list(self.__posts)):
                self.__posts[nick] = []
                self.__posts[nick].append(p)
            else:
                self.__posts[nick].append(p)


    def users(self):
        """
        """
        return list(self.__usuaris)

    def posts(self):
        """
        """
        return self.__posts

    def llistarPostsUser(self, nick):
        """
        """
        if nick not in list(self.__usuaris):
            return "Usuari no existeix"

        else:

            aux = []
            for x in self.__usuaris[nick]:
                aux.append(x.getContent())

            return "Posts de l'usuari " + nick + ": " + str(aux)


if __name__=='__main__':
    i = iTicApp()
    i.afegeixUsuari('Bernat', 'b@gmail.com', 'bbrunet')
    i.afegeixHastag("muntanya")
    i.publicarPost("pere","muntanya","into the wild")
    i.publicarPost("Bernat","muntanya","into the wild")
    i.publicarPost("Bernat","muntnya","into th wild")
    print(i.users())
    print(i.posts())
    print(i.llistarPostsUser("Bernat"))
