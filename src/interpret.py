"""
===============
Mòdul Interpret
===============
"""

class Interpret(object):
    """

    Classe Interpret

    >>> i = Interpret()
    >>> i.setPrompt(">>> ")
    >>> i.run()

    """

    def __init__(self):
        """

        >>> i = Interpret()
        >>> i.setPrompt(">>> ")
        >>> i.run()
        """
        self.__prompt = "~: "
        self.__dcom = {}

    def setPrompt(self, p):
        """
        Canvia el prompt de l'interpret (~: <- per defecte)

        >>> i = Interpret()
        >>> i.setPrompt(p)
        >>> i.__prompt
        p
        """
        self.__prompt = p

    def afegeixOrdre(self, nomc, ordre):
        """
        Afegeix ordre al diccionari, assignant paraula clau: nom de l'ordre i ordre: funcio

        >>> i = Interpret()
        >>> i.setPrompt(">>> ")
        >>> i.afegeixOrdre("usuari", xxss.afegeixUsuari)
        """
        self.__dcom[nomc] = ordre

    def run(self):
        """
        Classic "caixer", aplica la logica necessaria per a poder interpretar les ordres i els arguments introduits

        >>> i = Interpret()
        >>> i.setPrompt(">>> ")
        >>> i.run()
        """
        ordre = ""
        semafor = True

        while (semafor):
            ordre = input(self.__prompt)

            if (ordre.split(" ")[0] in self.__dcom.keys()):
                aux = ordre.split(" ")

                if (aux[0] == "usuari"):
                    self.__dcom[aux[0]](aux[1])

                elif (aux[0] == "hashtag"):
                    self.__dcom[aux[0]](aux[1])

                elif (aux[0] == "publicar"):
                    self.__dcom[aux[0]](aux[1],aux[2],aux[3])  # nick, id hashtag, contingut

                elif (aux[0] == "help"):
                    print("Les ordres disponibles son: " + str(self.__dcom.keys()))

                elif (aux[0] == "users" or aux[0] == "posts" or aux[0] == "posts-user" or aux[0] == "hashtags"):
                    print("Error de sintaxi a l'ordre " + aux[0] + ", falta el 'print'")

                elif (aux[0] == "print"):
                    if (aux[1] == "users"):
                        print(self.__dcom[aux[1]]())

                    elif(aux[1] == "posts"):
                        print(self.__dcom[aux[1]]())

                    elif(aux[1] == "posts-user"):
                        print(self.__dcom[aux[1]](aux[2]))

                    elif(aux[1] == "hashtags"):
                        print(self.__dcom[aux[1]]())

                    else:
                        print("Error de sintaxi al l'ordre print")


            elif (ordre == "surt"):
                semafor = False
                print("Fins aviat!")

            else:
                print("Ordre no trobada")
