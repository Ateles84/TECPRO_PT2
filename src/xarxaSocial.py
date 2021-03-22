"""
==================
Mòdul Xarxa Social
==================
"""
from usuari import Usuari
from posts import Posts
from hashtag import Hashtag

class iTicApp(object):
    """
    
    Classe iTicApp

    """
    def __init__(self):
        self.__usuaris = {}
        self.__posts = {}
        self.__hashtags = {}

    def afegeixUsuari(self,nick, email="", password=""):
        """
        """
        if nick in self.__usuaris.keys():
            return "Usuari ja existent"
        else:
            u = Usuari(nick, email, password)
            self.__usuaris[nick] = u

    def afegeixUsuari(self,nick):
        """
        """
        if nick in self.__usuaris.keys():
            return "Usuari ja existent"
        else:
            u = Usuari(nick)
            self.__usuaris[nick] = u

    def afegeixHashtag(self, id):
        """
        """
        if id in self.__hashtags.keys():
            return "Hashtag ja existent"
        else:
            h = Hashtag(id)
            self.__hashtags[id] = h

    def publicarPost(self, nick, id_hashtag, contingut_post):
        """
        """
        if nick not in list(self.__usuaris):
            print("Usuari no creat")
        else:
            p = Posts(contingut_post)
            p.registraUsuari(nick)
            p.registraHashtag(Hashtag(id_hashtag))

            self.__usuaris[nick].registraPost(p)

            if (nick not in list(self.__posts)):
                self.__posts[nick] = []
                self.__posts[nick].append(p)
            else:
                self.__posts[nick].append(p)


    def users(self):
        """
        """
        return str(list(self.__usuaris))

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
            return str(self.__usuaris[nick])
            """
            aux = []
            for x in self.__usuaris[nick]:
                aux.append(x.getContent())

            return "Posts de l'usuari " + nick + ": " + str(aux)
            """

if __name__=='__main__':
    i = iTicApp()
    i.afegeixUsuari('Bernat', 'b@gmail.com', 'bbrunet')
    i.afegeixHashtag("muntanya")
    i.publicarPost("pere","muntanya","into the wild")
    i.publicarPost("Bernat","muntanya","into the wild")
    #i.publicarPost("Bernat","mutnya","into th wild")
    print(i.users())
    print(i.posts())
    print(i.llistarPostsUser("Bernat"))
