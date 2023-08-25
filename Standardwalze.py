from Walze import Walze
from CONSTANTS import STANDARDWALZENTYP, ALPHABET

class Standardwalze(Walze):

    def __init__(self, type, ringstellung, grundstellung):
        """Constructor de rueda estardar
            type: Tipo de rueda {0 - 2}
            ringstellung: Posicion del anillo {A - Z}
            grundstellung: Posicion inicial del rotor {A - Z}
        """
        super().__init__(STANDARDWALZENTYP[type][0], ringstellung, grundstellung)
        self.__notch_positions = STANDARDWALZENTYP[type][1]
        self.__has_rotated = False


    def is_in_notch_position(self):
        """Verifica si un rotor se encuentra en posicion de giro"""
        for notch in self.__notch_positions:
            if self._Walze__stellung == notch:
                return True
        return False

    def rotate(self):
        """Induce la rotacion en el rotor"""
        if(self.__has_rotated == False):
            self._Walze__stellung = (self._Walze__stellung + 1) % len(ALPHABET)
            self.__has_rotated = True

    def reset(self):
        """Indica si un rotor ha rotado en la iteracion actual"""
        self.__has_rotated = False
