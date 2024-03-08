import os

restaurantes = ['Fogão a Lenha','Freguesão', 'Drinks Bar']


def exibir_nome_do_programa():  
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")

def finalizar_app():
    os.system('cls')
    print('Encerrando o programa')


def exibir_opcoes():
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Cadastrar Restaurante')
    print('4. Sair\n')

def opcao_invalida():
    print('Opcão invalida!')
    input('Digite uma tecla para voltar ao menu principal: ')
    main()

def cadastrar_nome_restaurante():
    os.system('cls')
    print('Cadastro de novos restaurantes\n')
    nome_restaurante = input('Digite o nome do Restaurante: ')
    restaurantes.append(nome_restaurante)
    print(f'O restaurante {nome_restaurante} foi cadastrado!!')
    input('\nDigite qualquer tecla para voltar ao menu inicial: ')
    main()

def listar_restaurantes():
    os.system('cls')
    print('Listando os restaurantes \n')

    for restaurante in restaurantes:  #para cada restaurante na lista restaurantes
        print(f'.{restaurante}')

    input('Digite uma tecla para voltar ao menu principal: ')
    main()



def escolher_opcao():
    try:
        opcao = int(input('Escolha uma opção: '))
        print(f'Você escolheu a opção {opcao}')


        if opcao == 1:
            cadastrar_nome_restaurante()
        elif opcao == 2:
            listar_restaurantes()
        elif opcao == 3:
            print('3. Cadastrar Restaurante')
        elif opcao == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()


def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()

    










