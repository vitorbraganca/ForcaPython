
import random

# Desenho da forca em ASCII art // Baseado em um programa em: https://codereview.stackexchange.com/questions/101968/hangman-with-ascii \\
art_forca = ["""
   _________
    |/        
    |              
    |                
    |                 
    |               
    |                   
    |___                 
    """,
"""
   _________
    |/   |      
    |              
    |                
    |                 
    |               
    |                   
    |___                 
    """,
"""
   _________       
    |/   |              
    |   (_)
    |                         
    |                       
    |                         
    |                          
    |___                       
    """,
"""
   ________               
    |/   |                   
    |   (_)                  
    |    |                     
    |    |                    
    |                           
    |                            
    |___                    
    """,
"""
   _________             
    |/   |               
    |   (_)                   
    |   /|                     
    |    |                    
    |                        
    |                          
    |___                          
    """,
"""
   _________              
    |/   |                     
    |   (_)                     
    |   /|\                    
    |    |                       
    |                             
    |                            
    |___                          
    """,
"""
   ________                   
    |/   |                         
    |   (_)                      
    |   /|\                             
    |    |                          
    |   /                            
    |                                  
    |___                              
    """,
"""
   ________
    |/   |     
    |   (_)    
    |   /|\           
    |    |        
    |   / \        
    |               
    |___           
    """]

objetos = ['faca', 'carteira', 'mouse', 'teclado', 'caneta', 'copo', 'garrafa', 'pulseira', 'relogio',
'telefone', 'notebook','celular']

animais = ['girafa', 'elefante', 'babuino', 'cavalo', 'cachorro', 'gato', 'guepardo', 'jaguatirica',
'camelo', 'dromedario', 'pombo', 'papagaio', 'vaca', 'humano', 'cobra']

profissoes = ['dentista', 'professor', 'médico', 'arquiteto', 'engenheiro', 'bombeiro', 'policial', 'paramédico',
'socorrista', 'jornalista', 'jornaleiro', 'motorista', 'atendente', 'piloto', 'vendedor', 'lojista', 'garçom',
'garçonete', 'prefeito', 'assessor', 'consultor', 'desenvolvedor', 'programador']

cphumano = ['orelha', 'olho', 'boca', 'braço', 'perna', 'espinha', 'cabeça', 'mao',
'pele', 'maxilar', 'bochecha', 'pescoço', 'coxa']

jogadas = vitorias = 0
usuario = tema = ' '

#    Funcao Principal do programa
def main():
    global art_forca, jogadas, vitorias, usuario, tema  # Chamando variaveis para a funcao
    print('JOGO DA FORCA')
    usuario = input('Digite seu nome de usuario: ')  # Lendo nome do usuario
    tema = input('TEMA: |OBJETOS (0), ANIMAIS (1), PROFISSOES (2), CORPO HUMANO (3)| \n')
    tema = tema.upper()
    jogadas += 1  # Atribuindo jogada
    letras_erradas = ''  # variavel para letras erradas
    letras_acertadas = ''  # variavel para letras acertadas
    secreta = gera_secreta().upper()  # Chamando funcao para gerar aleatoriamente uma palavra
    jogando = True  # Atribuindo True para controle

    while jogando:  # enquanto estiver jogando,
        impressao_jogo(letras_erradas, letras_acertadas, secreta)  # Chamando funcao para impressao do jogo
        palpite = atribuicao_palpite(letras_erradas + letras_acertadas)  # Atribuicao de palpite conforme funcao

        if palpite in secreta:  # Se palpite estiver na palavra secreta
            letras_acertadas += palpite  # Incrementar o acerto nas letras acertadas

            if checa_vitoria(secreta, letras_acertadas):  # Verificacao se o jogo foi vencido
                print(f'Parabens! A palavra secreta era {secreta} | ! Voce ganhou!!')  # Impressao da palavra + mensagem de vitoria
                vitorias += 1  # Incrementando vitoria em 1
                jogando = False  # Nao esta mais jogando
        else:  # Se o palpite nao estiver na palavra scrta
            letras_erradas += palpite  #  Incrmentando erros

            if len(letras_erradas) == len(art_forca) - 1:  # Verifica se qntd de erros e igual qntd de membros na forca
                impressao_jogo(letras_erradas, letras_acertadas, secreta)  # Caso sim, imprime o jogo

                print('Voce exagerou o seu limite de palpites!')  # Imprime mensagem ao usuario que ultrapassou limite
                print(f'Depois de {str(len(letras_erradas))} letras erradas e {str(len(letras_acertadas))}', end = ' ')
                print(f'palpites corretos, a palavra era {secreta}.')

                jogando = False  # Nao esta mais jogando

        if not jogando:  # Se nao estiver jogando,
            if repetir_jogo():  # Pergunta se quer jogar novament, se sim:
                if trocar_tema():
                    tema = input('TEMA: |OBJETOS (0), ANIMAIS (1), PROFISSOES (2), CORPO HUMANO (3)| \n')
                jogadas += 1  # Atribuicao de jogadas para controle futuro
                letras_erradas = ''  # Reiniciando variavel de erros
                letras_acertadas = ''  # Reiniciando variavel de acertos
                jogando = True  # Usuario volta a jogar
                secreta = gera_secreta().upper()  # Gera nova palavra
            else:  # Caso nao queira mais jogar,
                print(f'{usuario}, voce jogou {jogadas} vezes e ganhou {vitorias} delas.')  # Impressao de resultados finais


def gera_secreta():  # Funcao para gerar palavra aleatoria dentro do tema escolhido
    global objetos, animais
    if tema == 'OBJETOS' or tema == '0':
        return objetos[random.randint(0, (len(objetos)-1))]
    elif tema == 'ANIMAIS' or tema == '1':
        return animais[random.randint(0, (len(animais)-1))]
    elif tema == 'PROFISSOES' or tema == '2':
        return profissoes[random.randint(0, (len(profissoes)-1))]
    elif tema == 'CORPO HUMANO' or tema == '3':
        return cphumano[random.randint(0, (len(cphumano)-1))]


def impressao_espaco(palavra):  # Funcao para impressao com espacos
    for letra in palavra:
        print(letra, end = ' ')

    print()  # Deixa uma linha vazia


def impressao_jogo(letras_erradas, letras_acertadas, secreta):  # Funcao para impressao do jogo

    global art_forca  # defi uma variavel global
    print(art_forca[len(letras_erradas)] + '\n')  # Impressao da forca de acordo com erros do usuario

    print("Letras Erradas:", end = ' ')  # Impressao das letras erradas que o usuario digitou
    impressao_espaco(letras_erradas)  # Usando funcao para impressao com espacos

    vazio = '_' * len(secreta)  # Imprimindo um espaco vazio para cada letra que estiver na palavra secreta
    for i in range(len(secreta)):  # Para cada entrada do usuario, checar no comprimento palvra
        if secreta[i] in letras_acertadas:  # Checa se o indice esta em letras acertadas
            vazio = vazio[:i] + secreta[i] + vazio[i + 1:]  # Caso sim, adiciona ao indice e incrementa um

    impressao_espaco(vazio)  # Usando funcao para impressao com espacos


def atribuicao_palpite(palpite_usuario):

    while True:  # Enquanto usuario estiver dando palpites
        palpite = input('Entre com alguma letra. \n').upper()  # Lendo entrada do usuario e convertendo em maisucula
        if len(palpite) != 1:  # Verifica se usuario entrou com apenas uma letra
            print('Coloque uma unica letra')
        elif palpite in palpite_usuario:  # Verifica se usuario entrou com palpite repetido
            print('Voce ja digitou essa letra, digite de novo!')
        elif not 'A' <= palpite <= 'Z':  # Verifica se esta dentro do alfbeto
            print('Digite somente uma letra!')
        else:
            return palpite  # Caso cumpra todos os requisitos, retorna palpite


def repetir_jogo():
    return input("Voce quer jogar novamente? (SIM ou NAO)\n").upper().startswith('S')  # Retorna resposta do usuario


def trocar_tema():
    return input("Voce quer trocar o tema? (SIM ou NAO)\n").upper().startswith('S')  # Retorna resposta do usuario


def checa_vitoria(secreta, letras_acertadas):
    venceu = True
    for letra in secreta:  # Checa cada letra da palavra secreta
        if letra not in letras_acertadas:  # E se nao estiver na palavra secreta,
            venceu = False  #  Venceu torna-se falso
            break  # Quebra da estrutura de repeticao

    return venceu  # retorna True se a letra estiver na secreta e caso contrario, False


main()  # Chama funcao principal do programa
