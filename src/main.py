"""
==========
Mòdul Main
==========

El mòdul main no conté cap doctest
"""

from interpret import Interpret
from xarxaSocial import iTicApp

if __name__ == '__main__':
    xxss = iTicApp()

    i = Interpret()
    i.setPrompt("~: ")

    i.afegeixOrdre("usuari", xxss.afegeixUsuari)
    i.afegeixOrdre("hashtag", xxss.afegeixHashtag)
    i.afegeixOrdre("publicar", xxss.publicarPost)
    i.afegeixOrdre("print", "cyka blyat")
    i.afegeixOrdre("users", xxss.users)
    i.afegeixOrdre("posts", xxss.posts)
    i.afegeixOrdre("posts-user", xxss.llistarPostsUser)

    i.run()
