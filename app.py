import os

restaurantes = [{'Nome': 'Praça', 'Categoria': 'Japonesa', 'Ativo': False}, 
                {'Nome': 'Pizza Hut', 'Categoria': 'Pizzaria', 'Ativo': True},
                {'Nome': 'Haburguer`s Veg', 'Categoria': 'Lanches', 'Ativo': False}]

def exibir_nome_programa():
    print("""
██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
""")

def exibir_opcoes():
    print('1. Cadastrar restaurantes')
    print('2. Listar restaurantes')
    print('3. Alternar estado do restaurante')
    print('4. sair\n')

def finalizar_app():
    exibir_sub('\nFinalizando o app')

def voltar_menu():
    input('\nDigite uma tecla para voltar ao menu principal')
    main()

def opcao_invalida():
    print('Opção inválida!\n')
    voltar_menu()
    
def exibir_sub(texto):
    os.system('cls')
    linha = '*' * (len(texto) + 1)
    print (linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    exibir_sub('Cadastro de novos restaurantes')
    
    nome_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_restaurante}: ')
   
    dados_restaurante = {'Nome': nome_restaurante, 'Categoria': categoria, 'Ativo': False}
    restaurantes.append(dados_restaurante)
    
    print(f'\nO restaurante {nome_restaurante} foi cadastrado com sucesso!\n')
    
    voltar_menu()
    
def listar_restaurantes():
    exibir_sub('Listando restaurantes')
    
    print(f'{'nome do restaurante'.ljust(20)} | {'categoria'.ljust(18)} | Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['Nome']
        categoria = restaurante['Categoria']
        ativo = 'Ativado' if restaurante['Ativo']  else 'Desativado'
        
        print(f'- {nome_restaurante.ljust(18)} | {categoria.ljust(18)} | {ativo}')
        
    voltar_menu()
    
def alternar_restaurante():
    exibir_sub('Alterando o estado do restaurante')
    
    nome_restaurante = input('Digite o nome do restaurante que deseja alternar o estado: ')
    restaurante_encontrado = False
        
    for restaurante in restaurantes:
        if nome_restaurante == restaurante ['Nome']:
            restaurante_encontrado = True
            restaurante['Ativo'] = not restaurante['Ativo']
            
            mensagem = f'O restaurente {nome_restaurante} foi ativado com sucesso!' if restaurante['Ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso!'
            print(mensagem)
        
        if not restaurante_encontrado:
            print('O restaurante não foi encontrado!')
            
    voltar_menu()
    
def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
            
        elif opcao_escolhida == 2: 
            listar_restaurantes()  
            
        elif opcao_escolhida == 3:
            alternar_restaurante()
            
        elif opcao_escolhida == 4:
            finalizar_app()
            
        else:
            opcao_invalida()
    except:
        opcao_invalida()
    
def main():
    os.system('cls')
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()
    
if __name__ == '__main__':
    main()