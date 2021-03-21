"""
============
Mòdul Usuari
============
"""

import string

class Usuari(object):
    """
    """

    def __init__(self, nick, email, password):
        """
        Constructor

        >>> u = Usuari('Bernat', 'b@gmail.com', 'bbrunet')
        >>> u.nick
        'Bernat'
        """
        self.nick = nick
        self.__email = email
        self.__password = password

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
            #c=string.ascii_letters[c]
            #encPass=encPass+str(string.ascii_letters[(c+4)/26])

        return "Usuari: "+self.nick+" Email: "+self.__email+" Encripted password: "+encPass

    def lel(self):
        print("vaya tolo")

if __name__=='__main__':
    u = Usuari('Bernat', 'b@gmail.com', 'bbrunet')
    print(u)
