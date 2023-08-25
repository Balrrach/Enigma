from CONSTANTS import ALPHABET
from Steckern import Steckern
from Standardwalze import Standardwalze
from Zusatzwalze import Zusatzwalze
from Umkehrwalze import Umkehrwalze


class Enigma:

    def __init__(self, umkehrwalze_conf, zusatzwalze_conf, walzenlage_conf, ringstellung_conf, grundstellung_conf, steckern_conf):
        """Máquina Enigma M4 constructor
            umkehrwalze_conf: Tipo de reflector {Thin B, Thin C}
            zusatzwalze_conf: Tipo de rueda griega {Beta, Gamma}
            walzenlage_conf: Tipo de ruedas estandar [{1 - 8}](3)
            ringstellung_conf: Configuracion del anillo interior [{A - Z}](4)
            grundstellung_conf: Configuracion inicial [{A - Z}](4)
            steckern_conf: Configuracion del zocalo de clavijas [{A - Z}{A - Z}](10)
        """
        self.__umkehrwalze = Umkehrwalze(umkehrwalze_conf)
        self.__zusatzwalze = Zusatzwalze(zusatzwalze_conf, ringstellung_conf[0], grundstellung_conf[0])
        self.__standardwalze = [Standardwalze(walzenlage_conf[i], ringstellung_conf[i+1], grundstellung_conf[i+1]) for i in reversed(range(len(walzenlage_conf)))]
        self.__steckern = Steckern(steckern_conf)

    def transform_to_M3(self):
        """Máquina Enigma M3 converter"""
        # La rueda griega necesita estar en concordancia con el tipo de reflector 
        swith = {
            'Thin B': 'Beta',
            'Thin C': 'Gamma',
        }
        zusatzwalze_conf  = swith[self.__umkehrwalze.get_type()]
        self.__zusatzwalze = Zusatzwalze(zusatzwalze_conf, 'A', 'A')

    def set_umkerwalze(self, umkehrwalze_conf):
        """Cambia la el reflector
            umkehrwalze_conf Tipo de reflector: {Thin B, Thin C}
        """
        self.__umkehrwalze = Umkehrwalze(umkehrwalze_conf)

    def set_zusatzwalze(self, zusatzwalze_conf, ringstellung_conf, grundstellung_conf):
        """Cambia la rueda griega
            zusatzwalze_conf: Tipo de rueda griega {Beta, Gamma}
            ringstellung_conf: Configuracion del anillo interior {A - Z}
            grundstellung_conf: Configuracion inicial {A - Z}
        """
        self.__zusatzwalze = Zusatzwalze(zusatzwalze_conf, ringstellung_conf, grundstellung_conf)

    def set_standarwalze(self, number, walzenlage_conf, ringstellung_conf, grundstellung_conf):
        """Cambia una de las ruedas estandard a eleccion
            number: Rueda estandard a modificar {0 - 2}
            walzenlage_conf: Tipo de rueda estandar {1 - 8}
            ringstellung_conf: Configuracion del anillo interior {A - Z}
            grundstellung_conf: Configuracion inicial {A - Z}
        """
        self.__standardwalze[number] = Standardwalze(walzenlage_conf, ringstellung_conf, grundstellung_conf)

    def set_grundstellung(self, grundstellung_conf):
        """Cambia la configuracion inicial de todas las ruedas
            grundstellung_conf: Configuracion inicial [{A - Z}](4)
        """
        self.__zusatzwalze.set_stellung(grundstellung_conf[0])
        for i in range(3):
            self.__standardwalze[i].set_stellung(grundstellung_conf[len(grundstellung_conf) - (i+1)])

    def reset(self):
        """Resetea la máquina a la configuración con la que fue creada"""
        self.__zusatzwalze.reset()
        for sw in self.__standardwalze:
            sw.reset()


    def __code_forward(self, letter):
        """Codifica una letra desde el zócalo de clavijas hasta la rueda griega
            letter: Letra a codificar
        """
        ret = self.__steckern.code(letter)
        
        for sw in self.__standardwalze:
            ret = sw.code_forward(ret)

        ret = self.__zusatzwalze.code_forward(ret)
                
        return ret

    def __code_backward(self, letter):
        """Codifica una letra desde la rueda griega hasta el zócalo de clavijas
            letter: Letra a codificar
        """
        ret = self.__zusatzwalze.code_backward(letter)

        for sw in reversed(self.__standardwalze):
            ret = sw.code_backward(ret)
        
        ret = self.__steckern.code(ret)
        
        return ret

    def __rotate(self):
        """Rota los rotores de acuerdo al mecanismo de la maquina"""
        for i in reversed(range(2)):
            if(self.__standardwalze[i].is_in_notch_position()):
                self.__standardwalze[i].rotate()
                self.__standardwalze[i+1].rotate()

        self.__standardwalze[0].rotate()

        self.__reset_walzen()

    def __reset_walzen(self):
        for standard_walzen in self.__standardwalze:
            standard_walzen.reset()
        
    def __code_letter(self, letter):
        """Codifica una letra
            letter: Letra a codificar. Si el simbolo no esta en el alfabeto sera ignorado
        """

        if not letter in ALPHABET:
            return letter

        self.__rotate()
        ret = self.__code_forward(letter)
        ret = self.__umkehrwalze.code(ret)
        ret = self.__code_backward(ret)

        return ret

    def code_text(self, text):
        """Codifica un texto
            text: Texto a codificar {string}
        """

        coded_text = ''.join([self.__code_letter(letter) for letter in text])
        self.reset()

        return coded_text
