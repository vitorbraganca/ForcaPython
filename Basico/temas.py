import random
objetos = 'faca carteira mouse teclado caneta copo garrafa pulseira relogio'.split()
animais = 'girafa elefante babuino cavalo cachorro guepardo jaguatirica camelo dromedario'.split()
tema = input('TEMA: ')
tema = tema.upper()


def gera_palavra():
    global objetos, animais
    if tema == 'OBJETOS':
        return random.choice(objetos)
    elif tema == 'ANIMAIS':
        return random.choice(animais)

palavra_secreta = gera_palavra().upper()
print('PALAVRA SECRETA: ', palavra_secreta)
