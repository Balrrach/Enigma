from Walze import Walze
from CONSTANTS import ZUSATZWALZENTYP

class Zusatzwalze(Walze):

    def __init__(self, type, ringstellung, grundstellung):
        """Constructor de rueda estardar
            type: Tipo de rueda {0 - 2}
            ringstellung: Posicion del anillo {A - Z}
            grundstellung: Posicion inicial del rotor {A - Z}
        """
        super().__init__(ZUSATZWALZENTYP[type], ringstellung, grundstellung)
