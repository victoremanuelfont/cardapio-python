import os

restaurantes = [{'nome':'Fogão a Lenha', 'categoria':'churrasco', 'ativo': False},
                {'nome':'Drinks Bar', 'categoria':'noite', 'ativo': True},
                {'nome':'Rancho do Serjão', 'categoria':'dia', 'ativo': True}]


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

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal: ')
    main()

def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)

def exibir_opcoes():
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Cadastrar Restaurante')
    print('4. Sair\n')

def opcao_invalida():
    print('Opcão invalida!')
    voltar_ao_menu_principal()

def cadastrar_nome_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes\n')
    nome_restaurante = input('Digite o nome do Restaurante: ')
    restaurantes.append(nome_restaurante)
    print(f'O restaurante {nome_restaurante} foi cadastrado!!')
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Listando os restaurantes \n')

    for restaurante in restaurantes:  #para cada restaurante na lista restaurantes
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = restaurante['ativo']
        print(f'-{nome_restaurante} | {categoria} | {ativo}')

    voltar_ao_menu_principal()

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

    










