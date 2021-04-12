"""
==================
Mòdul Xarxa Social
==================
"""
from usuari import Usuari
from posts import Posts
from hashtag import Hashtag
import pickle

class iTicApp(object):
    """

    Classe iTicApp

    """
    def __init__(self):
        self.__usuaris = {}
        self.__posts = {}
        self.__hashtags = {}

    def afegeixUsuari(self,nick, email, password):
        """
        Aquest metode no es fa servir, ja que per a fer servir l'interpret nomes es fa servir el metdoe d'abaix

        >>> i = iTicApp()
        >>> i.afegeixUsuari('Bernat')
        >>> i.users()
        "['Bernat']"
        """
        if nick in self.__usuaris.keys():
            print("Usuari ja existent")
        else:
            u = Usuari(nick, email, password)
            self.__usuaris[nick] = u

    def afegeixUsuari(self,nick):
        """
        Aprofitant el metode anterior, afegim aquest amb sobrecarrega per a que faci la funcionalitat a l'interpret

        >>> i = iTicApp()
        >>> i.afegeixUsuari('Bernat')
        >>> i.users()
        "['Bernat']"
        """
        if nick in self.__usuaris.keys():
            print("Usuari ja existent")
        else:
            u = Usuari(nick)
            self.__usuaris[nick] = u

    def afegeixHashtag(self, id):
        """
        S'afeig el Hashtag al diccionari corresponent, no es fa servir mai

        >>> i = iTicApp()
        >>> i.afegeixHashtag('munta')
        >>> i.afegeixHashtag('munta')
        Hashtag ja existent
        """
        if id in self.__hashtags.keys():
            print("Hashtag ja existent")
        else:
            h = Hashtag(id)
            self.__hashtags[id] = h

    def publicarPost(self, nick, id_hashtag, contingut_post):
        """
        Metode que registra posts a partir d'un usuari i d'un hashtag, el Doctest no llista usuaris ja que el timestamp no sera mai igual

        >>> i = iTicApp()
        >>> i.publicarPost('Bernat', 'munta', 'bon diaaa' )
        Usuari no creat
        """
        if nick not in list(self.__usuaris):
            print("Usuari no creat")
        else:
            p = Posts(contingut_post,id_hashtag)
            p.registraUsuari(nick)

            if (id_hashtag not in self.__hashtags.keys()):
                print("Hashtag no creat")
                self.__hashtags[id_hashtag] = Hashtag(id_hashtag)
                p.registraHashtag(Hashtag(id_hashtag))
                self.__hashtags[id_hashtag].hashTagUtilitzat()

            else:
                self.__hashtags[id_hashtag].hashTagUtilitzat()

            self.__usuaris[nick].registraPost(p)

            if (nick not in list(self.__posts)):
                self.__posts[nick] = []
                self.__posts[nick].append(p)
            else:
                self.__posts[nick].append(p)

    def users(self):
        """
        Metode que retorna una llista en forma d'str amb tots els usuaris registrats a la xarxa social

        >>> i = iTicApp()
        >>> i.afegeixUsuari('Bernat')
        >>> i.users()
        "['Bernat']"
        """
        return str(list(self.__usuaris))

    def posts(self):
        """
        Metode que retorna un diccionari amb tots els posts registrats a la xarxa social


        >>> i = iTicApp()
        >>> i.afegeixUsuari('Bernat')
        >>> i.afegeixHashtag('munta')
        >>> i.publicarPost('Bernat', 'munta', 'bon diaaa' )
        >>> i.posts()
        {'Bernat': [Post id: 1 | Usuari: Bernat | info: bon diaaa | Hashtag: [#munta] | Date: Wed Mar 24 08:31:49 2021]}
        """
        return self.__posts

    def hashtags(self):
        """
        Metode que retorna un diccionari amb tots els hashtags registrats a la xarxa social

        >>> i = iTicApp()
        >>> i.afegeixUsuari('Bernat')
        >>> i.afegeixHashtag('munta')
        >>> i.publicarPost('Bernat', 'munta', 'bon diaaa' )
        >>> i.hashtags()
        '#munta | cops utilitzat: 1 '

        """
        aux = ""
        for x in self.__hashtags.keys():
            aux += str(self.__hashtags[x]) + " | "
        return aux[0:len(aux)-2]

    def llistarPostsUser(self, nick):
        """
        Metode que retorna una llista en forma d'str l'objecte usuari, aixo es degut a que a la tasca 5 es demana que cada objecte Usuari tingui tots els posts en una llista

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


    def desa(self):
        """
        Hem recorregut a l'eina Pickle al trobar la dificultat de llegir un diccionari d'un arxiu amb l'usuari formatejat per el metode __str__,
        L'idea ve de poder guardar objectes a arxius en forma de dades binaries:
        https://stackoverflow.com/questions/4529815/saving-an-object-data-persistence

        Desa la xarxa ’self’ en un fitxer de text. El fitxer ha d’estar obert en mode escriptura.

        """
        f = "data.dat"

        with open(f, 'wb') as output:
            pickle.dump(self.__usuaris, output, pickle.HIGHEST_PROTOCOL)
            pickle.dump(self.__posts, output, pickle.HIGHEST_PROTOCOL)
            pickle.dump(self.__hashtags, output, pickle.HIGHEST_PROTOCOL)

    def obre(self):
        """
        Afegeix a la xarxa ’self’ els usuaris i posts que hi ha en el fitxer de text.
        El fitxer ha d’estar oberten mode lectura.

        """
        f = "data.dat"

        with open(f, 'rb') as input:
            self.__usuaris = pickle.load(input)
            self.__posts = pickle.load(input)
            self.__hashtags = pickle.load(input)
