ListaProdutos = [] #dentro de um array
 
def cadastra_produto(produto_para_cadastrar: dict):
    ListaProdutos.append(produto_para_cadastrar)
    return
 
opcao = int(input('Deseja cadastrar um novo produto? 0 - Não     1 - Sim '))
while opcao == 1:
    novoProduto = {}
    
    novoProduto['codigo'] = int(input('Digite o código do produto: '))
    
    if novoProduto['codigo'] == 0:
        print('Código 0, FIM DE CADASTRO DE PRODUTOS')
        break
    #Recebimentos de informações
    novoProduto['estoque'] = int(input('Qual a quantidade em estoque: '))
    novoProduto['minimo'] = int(input('Qual a quantidade mínima do estoque: '))
    
    cadastra_produto(novoProduto)
    opcao = int(input('Deseja cadastrar um novo produto? 0 - Não     1 - Sim '))
#Se a lista de produtos for maior que 0
if len(ListaProdutos) > 0:
    print('Código em ordem crescente:')
    print("Código do produto".center(10), end='')
    print("Estoque".center(10), end='')
    print("Mínimo".center(10))
#laço de repetição
    for produto in sorted(ListaProdutos, key=lambda item: item['codigo']):
        print(str(produto['codigo']).center(10), end='')
        print(str(produto['estoque']).center(10), end='')
        print(str(produto['minimo']).center(10))
else: #Nada digitado vai cair aqui
    print('A lista de produtos esta vazia.')
