"""
============
Mòdul Usuari
============
"""

import string

class Usuari(object):
    """
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
        self.__posts.append(post)


    def __str__(self):
        """
        Converteix l'objecte a cadena
        :rtype: str

        >>> u = Usuari('Bernat', 'b@gmail.com', 'bbrunet')
        >>> print(u)
        Usuari: Bernat Email: b@gmail.com Encripted password: *******

        """
        encPass=""
        for c in self.__password:
            encPass=encPass+"*"

            #" | Email: " + self.__email + " | Encripted password: " + encPass +
        return "Usuari: " + self.nick + " | Posts: " + str(self.__posts)


if __name__=='__main__':
    u = Usuari('Bernat', 'b@gmail.com', 'bbrunet')
    print(u)
