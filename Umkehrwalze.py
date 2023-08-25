from CONSTANTS import UMKEHRWALZENTYP, ALPHABET

class Umkehrwalze:

    def __init__(self, type):
        """Constructor del Reflector
            type: Tipo de reflector{Thin B, Thin C}
        """
        self.__type = type
        self.__permutation = UMKEHRWALZENTYP[type]

    def get_type(self):
        """Devuelve el tipo de reflector"""
        return self.__type

    def code(self, letter):
        """Devuelve la letra asociada segun el reflector
            letter: letra de la que se busca la pareja: {A - Z}
        """
        return self.__permutation[ALPHABET.index(letter)]
