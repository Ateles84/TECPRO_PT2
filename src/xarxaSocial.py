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

        >>> i = iTicApp()
        >>> i.afegeixUsuari('Bernat', 'b@gmail.com', 'bbrunet')
        """
        if nick in self.__usuaris.keys():
            return "Usuari ja existent"
        else:
            u = Usuari(nick, email, password)
            self.__usuaris[nick] = u

    def afegeixUsuari(self,nick):
        """

        >>> i = iTicApp()
        >>> i.afegeixUsuari('Bernat')
        """
        if nick in self.__usuaris.keys():
            return "Usuari ja existent"
        else:
            u = Usuari(nick)
            self.__usuaris[nick] = u

    def afegeixHashtag(self, id):
        """

        >>> i = iTicApp()
        >>> i.afegeixHashtag('munta')
        """
        if id in self.__hashtags.keys():
            return "Hashtag ja existent"
        else:
            h = Hashtag(id)
            self.__hashtags[id] = h

    def publicarPost(self, nick, id_hashtag, contingut_post):
        """

        >>> i = iTicApp()
        >>> i.afegeixUsuari('Bernat')
        >>> i.afegeixHashtag('munta')
        >>> i.publicarPost('Bernat', 'munta', 'bon diaaa' )
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

        >>> i = iTicApp()
        >>> i.afegeixUsuari('Bernat')
        >>> i.users()
        "['Bernat']"
        """
        return str(list(self.__usuaris))

    def posts(self):
        """

        >>> i = iTicApp()
        >>> i.afegeixUsuari('Bernat')
        >>> i.afegeixHashtag('munta')
        >>> i.publicarPost('Bernat', 'munta', 'bon diaaa' )
        >>> i.posts()
        {'Bernat': [Post id: 1 | Usuari: Bernat | info: bon diaaa | Hashtag: [#munta] | Date: Tue Mar 23 18:25:36 2021]}

        """
        return self.__posts

    def llistarPostsUser(self, nick):
        """

        >>> i = iTicApp()
        >>> i.afegeixUsuari('Bernat')
        >>> i.afegeixHashtag('munta')
        >>> i.publicarPost('Bernat', 'munta', 'bon diaaa' )
        >>> i.llistarPostsUser('Bernat')
        'Usuari: Bernat | Posts: [Post id: 1 | Usuari: Bernat | info: bon diaaa | Hashtag: [#munta] | Date: Tue Mar 23 18:27:06 2021]'
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
