from Enigma import Enigma

def main():
    # Crear una instancia de una máquina con la configuración deseada
    enigma = Enigma('Thin C', 'Beta', '568', 'EPEL', 'NAEM', 'AE BF CM DQ HU JN LX PR SZ VW')

    # Obtener configuración
    print("Clave procesada: " + enigma.code_text("QEOB") + "\n")

    # Ajustar la nueva posicion inicial
    enigma.set_grundstellung('CDSZ')

    # Se lee el texto a procesar
    preprocess_sendschreiben = open("processed_sendschreiben.txt").read()

    # Se eliminan los primeros y ultimos dos grupos del mensaje
    sendschreiben = preprocess_sendschreiben[10:len(preprocess_sendschreiben)-10]

    # Se procesa el mensaje
    print("Mensaje procesado: \n" + enigma.code_text(sendschreiben) + "\n")

    # Reseteo de la maquina
    enigma.reset()

    # Cambion de reflector
    enigma.set_umkerwalze('Thin B')
    # Cambio de rueda griegra
    enigma.set_zusatzwalze('Gamma', 'B', 'G')
    # Cambio del tercer rotor
    enigma.set_standarwalze(2, '5', 'L', 'W')

    # Cambio de la posicion inicial
    enigma.set_grundstellung('ABCD')

    # Transformacion a una M3
    enigma.transform_to_M3()


if __name__=="__main__":
    main()
