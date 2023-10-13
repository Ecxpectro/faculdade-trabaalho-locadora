from utils import config
from utils.splash_screen import SplashScreen
from reports.relatorios import Relatorio
from controller.controller_movie_type import Controller_MovieType
from controller.controller_user import Controller_User
from controller.controller_movie import Controller_Movie
from controller.controller_user_movie import Controller_User_movie
tela_inicial = SplashScreen()
relatorio = Relatorio()
ctrl_movie_type = Controller_MovieType()
ctrl_user = Controller_User()
ctrl_movie = Controller_Movie()
ctrl_user_movie = Controller_User_movie()

def reports(opcao_relatorio:int=0):

    if opcao_relatorio == 1:
        relatorio.get_relatorio_user()          
    elif opcao_relatorio == 2:
        relatorio.get_movie_type_data()
    elif opcao_relatorio == 3:
        relatorio.get_movie_data()
    elif opcao_relatorio == 4:
        relatorio.get_sales_data()

        

def inserir(opcao_inserir:int=0):

    if opcao_inserir == 1:                               
        novo_user = ctrl_user.inserir_user()
    elif opcao_inserir == 2:
        novo_movie_type= ctrl_movie_type.insert_movie_type()
    elif opcao_inserir == 3:
        relatorio.get_movie_type_data()
        novo_movie = ctrl_movie.insert_movie()
    elif opcao_inserir == 4:
        nova_venda = ctrl_user_movie.insert_sale()


        

def atualizar(opcao_atualizar:int=0):

    if opcao_atualizar == 1:
        relatorio.get_user_data()
        usuario_atualizado = ctrl_user.update_user()
    elif opcao_atualizar == 2:
        relatorio.get_movie_type_data()
        cliente_atualizado = ctrl_movie_type.update_movie_type()
    elif opcao_atualizar == 3:
        relatorio.get_movie_data()
        movie_atualizado = ctrl_movie.update_movie()

 

def excluir(opcao_excluir:int=0):

    if opcao_excluir == 1:
        relatorio.get_movie_type_data()
        ctrl_movie_type.delete_movie_type()
            
       


def run():
    print(tela_inicial.get_updated_screen())
    config.clear_console()

    while True:
        try:
            print(config.MENU_PRINCIPAL)
            opcao = int(input("Escolha uma opção [1-5]: "))
            config.clear_console(1)
            
            if opcao == 1: # Relatórios
                print(config.MENU_RELATORIOS)
                opcao_relatorio = int(input("Escolha uma opção [0-6]: "))
                config.clear_console(1)

                reports(opcao_relatorio)

                config.clear_console(1)

            elif opcao == 2: # Inserir Novos Registros
                print(config.MENU_ENTIDADES)
                opcao_inserir = int(input("Escolha uma opção [1-4]: "))
                config.clear_console(1)

                inserir(opcao_inserir=opcao_inserir)

                config.clear_console()
                print(tela_inicial.get_updated_screen())
                config.clear_console()

            elif opcao == 3: # Atualizar Registros
                print(config.MENU_ENTIDADES)
                opcao_atualizar = int(input("Escolha uma opção [1-3]: "))
                config.clear_console(1)

                atualizar(opcao_atualizar=opcao_atualizar)

                config.clear_console()

            elif opcao == 4:
                print(config.MENU_ENTIDADES)
                opcao_excluir = int(input("Escolha uma opção [1]: "))
                config.clear_console(1)

                excluir(opcao_excluir=opcao_excluir)

                config.clear_console()
                print(tela_inicial.get_updated_screen())
                config.clear_console()

            elif opcao == 5:
                print(tela_inicial.get_updated_screen())
                config.clear_console()
                print("Obrigado por utilizar o nosso sistema.")
                exit(0)

            else:
                print("Opção incorreta. Por favor, escolha uma opção válida.")

        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro.")


if __name__ == "__main__":
    run()