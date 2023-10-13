MENU_PRINCIPAL = """Menu Principal
1 - Relatórios
2 - Inserir Registros
3 - Atualizar Registros
4 - Remover Registros
5 - Sair
6 - Realizar Venda
"""

MENU_RELATORIOS = """Relatórios
1 - Relatório de Pedidos por Fornecedores
2 - Relatório de Pedidos
3 - Relatório de Produtos
4 - Relatório de Clientes
5 - Relatório de Fornecedores
6 - Relatório de Itens de Pedidos
7 - Relatório de Usuários
0 - Sair
"""

MENU_ENTIDADES = """Entidades
1 - PRODUTOS
2 - Gênero do filme
3 - FORNECEDORES
4 - PEDIDOS
5 - ITENS DE PEDIDOS
6 - Usuários
7 - Movie
8 - Venda
"""

# Consulta de contagem de registros por tabela
QUERY_COUNT = 'select count(1) as total_{tabela} from {tabela}'

def clear_console(wait_time:int=3):
    '''
       Esse método limpa a tela após alguns segundos
       wait_time: argumento de entrada que indica o tempo de espera
    '''
    import os
    from time import sleep
    sleep(wait_time)
    os.system("clear")