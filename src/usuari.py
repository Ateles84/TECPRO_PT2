"""
============
Mòdul Usuari
============
"""

import string

class Usuari(object):
    """

    Classe Usuari

    >>> u = Usuari('Bernat', 'b@gmail.com', 'bbrunet')
    >>> u.nick
    'Bernat'
    """

    def __init__(self, nick, email="", password=""):
        """
        Constructor

        >>> u = Usuari('Bernat', 'b@gmail.com', 'bbrunet')
        >>> u.nick
        'Bernat'
        """
        self.nick = nick
        self.__email = email
        self.__password = password
        self.__posts = []

    def registraPost(self, post):
        """
        Aquest metode afegeix un post a l'atribut Posts(llista) de l'usuari

        >>> u = Usuari('Bernat', 'b@gmail.com', 'bbrunet')
        >>> u.registraPost('bon diaaa')
        >>> u.getPosts()
        ['bon diaaa']
        """
        self.__posts.append(post)

    def getPosts(self):
        """
        Aquest metode torna l'objecte llista de l'atribut Posts
        
        >>> u = Usuari('Bernat', 'b@gmail.com', 'bbrunet')
        >>> u.getPosts()
        []
        """
        return self.__posts


    def __str__(self):
        """
        Converteix l'objecte a cadena
        :rtype: str

        >>> u = Usuari('Bernat', 'b@gmail.com', 'bbrunet')
        >>> print(u)
        Usuari: Bernat | Posts: []
        """
        encPass=""
        for c in self.__password:
            encPass=encPass+"*"

            #" | Email: " + self.__email + " | Encripted password: " + encPass +
        return "Usuari: " + self.nick + " | Posts: " + str(self.__posts)
