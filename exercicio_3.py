import random
 
doadores = [] #array que vai armazenar os dados dos doadores
 
def cadastra_doador(nome:str, doacao:float): #cadastro de doadores
    doadores.extend( ((nome + ' ') * int(doacao//10)).split() )
    return
 
def sorteia_ganhador():
    random.shuffle(doadores)
    print(f'Lista de doadores embaralhada: {doadores}')
    return random.choice(doadores)
 
opcao = int(input('Adcionar doador? 0 - Não     1 - Sim '))
 
while opcao == 1: #laço de repetição ate que a condição seja concluida
    doador = input('Digite o nome do doador: ')
    valor = float(input('Qual sera o valor da doacao? '))
    
    while len(doador.strip()) == 0 or valor < 10:
        print('valor mínimo para doação é de R$ 10')
        doador = input('Digite o nome do doador: ')
        valor = float(input('Qual sera o valor da doacao? '))
    
    cadastra_doador(doador, valor)
    
    opcao = int(input('Adcionar doador? 0 - Não     1 - Sim '))
 
if len(doadores) > 0:
    print(f'Lista de doadores para serem sorteiados: {doadores}')    
    print(f'O vencedor(a) foi: {sorteia_ganhador()}, Parabéns!!!')
