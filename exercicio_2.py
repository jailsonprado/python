#exercicio 2
 
def mail(nome:str, sobrenome:str, ru:str):
    return f"sr(a). {nome} {sobrenome}, seu email é {nome[0].lower() + sobrenome.lower() + ru[5:7] + '@algoritmos.com.br'}" 
    #usei o .lower para aparecer as letras em minusculo quando gerar o email #Nome[0] pegou a posição 0 da string, ru[5:7] pegou as duas ultimas posições do valor str
 
print(mail('Jailson', 'Prado', '3673912'))
 
