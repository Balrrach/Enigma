from CONSTANTS import ALPHABET

class Steckern:

    def __init__(self, steckern_conf):
        """Constructor del clavijero
            steckern_conf: Configuracion del clavijero [{A - Z}](10)
        """
        pairs = steckern_conf.split(' ')
        
        self.__permutation = list(ALPHABET)

        for pair in pairs:
            index0 = ALPHABET.index(pair[0])
            index1 = ALPHABET.index(pair[1])
            self.__permutation[index0] = ALPHABET[index1]
            self.__permutation[index1] = ALPHABET[index0]


    def code(self, letter):
        """Devuelve la pareja de una letra
            letter: Letra a la que encontrale la pareja {A - Z}
        """
        return self.__permutation[ALPHABET.index(letter)]
