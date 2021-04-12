"""
==========
Mòdul Main
==========

El mòdul main no conté cap doctest, de totes formes, es pot solicitar l'acces al Github del projecte a la seguent direccio: github.com/Ateles84/TECPRO_PT2
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
    i.afegeixOrdre("ajuda", "rush b fast")
    i.afegeixOrdre("users", xxss.users)
    i.afegeixOrdre("posts", xxss.posts)
    i.afegeixOrdre("posts-user", xxss.llistarPostsUser)
    i.afegeixOrdre("hashtags", xxss.hashtags)
    i.afegeixOrdre("desa", xxss.desa)
    i.afegeixOrdre("obre", xxss.obre)

    i.run()
