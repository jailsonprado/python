aluno = input('Qual nome do aluno? ')#Inserindo nome do aluno
nota = float(input('Qual foi a nota? ')) #inserindo nota
 
while (nota <= 10): # se nota for maior que 10, fim de programa!
    #Condições lógicas usadas exemplo : 0 maior ou igual a var nota menor ou igual a 2.9
    if (0 <= nota <=  2.9): 
            print('O aluno {} tirou {} e se enquadra no conceito  E'.format(aluno, nota))
 
    elif ( 3.0 <= nota <= 4.9):
            print('O aluno {} tirou {} e se enquadra no conceito  D'.format(aluno, nota))
 
    elif (5.0 <= nota <= 6.9):
            print('O aluno {} tirou {} e se enquadra no conceito  C'.format(aluno, nota))
            
 
    elif (7.0 <= nota <= 8.9):
            print('O aluno {} tirou {} e se enquadra no conceito  B'.format(aluno, nota))
 
    else:
            print('O aluno {} tirou {} e se enquadra no conceito  A'.format(aluno, nota))
#enquanto a nota for menor que 10, laço de repetição continua a executar
    aluno = input('Qual nome do aluno? ')
    nota = float(input('Qual foi a nota? '))
           
quit
print('Programa encerrado') 