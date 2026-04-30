import os

restaurantes = [{'Nome': 'Praça', 'Categoria': 'Japonesa', 'Ativo': False}, 
                {'Nome': 'Pizza Hut', 'Categoria': 'Pizzaria', 'Ativo': True},
                {'Nome': 'Haburguer`s Veg', 'Categoria': 'Lanches', 'Ativo': False}]

def exibir_nome_programa():
    print(""""
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
    print('3. Ativar restaurante')
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
    print(texto)
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
    
    for restaurante in restaurantes:
        nome_restaurante = restaurante['Nome']
        categoria = restaurante['Categoria']
        ativo = restaurante['Ativo']
        
        print(f'- {nome_restaurante} | {categoria} | {ativo}')
        
    voltar_menu()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            print ('\nCadastrar restaurantes\n')
            cadastrar_novo_restaurante()
            
            
        elif opcao_escolhida == 2:
            print('\nListar restaurantes\n') 
            listar_restaurantes()  
            
        elif opcao_escolhida == 3:
            print('\nAtivar restaurante\n')
            
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
    
    
    
    