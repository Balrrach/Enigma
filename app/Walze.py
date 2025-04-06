from CONSTANTS import ALPHABET

class Walze:
    def __init__(self, permutation, ringstellung, grundstellung):
        """Constructor de rueda estardar
            ringstellung: Posicion del anillo {A - Z}
            grundstellung: Posicion inicial del rotor {A - Z}
            permutation: Permutacion asociada a la rueda(Sus valores se concretan en las clases hijas)
        """
        self.__permutation = permutation
        self.__ringstellung = ALPHABET.index(ringstellung)
        self.__grundstellung = ALPHABET.index(grundstellung)
        self.__stellung = ALPHABET.index(grundstellung)


    def set_stellung(self, stellung):
        """Modifica la posicion actual del rotor"""
        self.__stellung = ALPHABET.index(stellung)

    def reset(self):
        """Devuelve el rotor a su posicion inicial"""
        self.__stellung = self.__grundstellung


    def code_forward(self, letter):
        """Codifica una letra que recorre cable en direccion al reflector"""
        return ALPHABET[ (ALPHABET.index(self.__permutation[(ALPHABET.index(letter) + self.__stellung - self.__ringstellung) % len(ALPHABET)]) - self.__stellung + self.__ringstellung) % len(ALPHABET) ]

    def code_backward(self, letter):
        """Codifica una letra que recorre cable en direccion al tablero de luces"""
        return ALPHABET[ (self.__permutation.index(ALPHABET[(ALPHABET.index(letter) + self.__stellung - self.__ringstellung) % len(ALPHABET)]) - self.__stellung + self.__ringstellung) % len(ALPHABET) ]
