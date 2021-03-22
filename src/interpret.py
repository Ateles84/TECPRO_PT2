class Interpret(object):
    """
    """

    def __init__(self):
        self.__prompt = ""
        self.__dcom = {}

    def setPrompt(self, p):
        self.__prompt = p

    def afegeixOrdre(self, nomc, ordre):
        self.__dcom[nomc] = ordre

    def run(self):

        ordre = ""
        semafor = True

        while (semafor):
            ordre = input(self.__prompt)


            if (ordre.split(" ")[0] in self.__dcom.keys()):
                aux = ordre.split(" ")

                if (aux[0] == "usuari"):
                    self.__dcom[aux[0]](aux[1])
                    print("entrem a usuari")

                elif (aux[0] == "hashtag"):
                    self.__dcom[aux[0]](aux[1])

                elif (aux[0] == "publicar"):
                    self.__dcom[aux[0]](aux[1],aux[2],aux[3])  # nick, id hashtag, contingut

                elif (aux[0] == "print"):
                    if (aux[1] == "users"):
                        print(self.__dcom[aux[1]]())
                        print("entrem a usuari")

                    elif(aux[1] == "posts"):
                        print(self.__dcom[aux[1]]())

                    elif(aux[1] == "posts-user"):
                        print(self.__dcom[aux[1]](aux[2]))

            elif (ordre == "surt"):
                semafor = False
                print("Cyka blyat")

            else:
                print("Ordre no trobada")



if __name__ == '__main__':
    i = Interpret()
    i.setPrompt(">>> ")
    i.run()