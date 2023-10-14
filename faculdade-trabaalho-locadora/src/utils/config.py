MENU_PRINCIPAL = """Menu Principal
1 - Relatórios
2 - Inserir Registros
3 - Atualizar Registros
4 - Remover Registros
5 - Sair
"""

MENU_RELATORIOS = """Relatórios
1 - Relatório de Usuários
2 - Relatório de Gênero de filmes
3 - Relatório de Filmes
4 - Relatório de Vendas
0 - Sair
"""

MENU_ENTIDADES_INSERT = """Entidades
1 - USUÁRIOS
2 - GÊNERO DO FILME
3 - FILME
4 - VENDAS
"""
MENU_ENTIDADES_UPDATE = """Entidades
1 - USUÁRIOS
2 - GÊNERO DO FILME
3 - FILME
"""
MENU_ENTIDADES_DELETE = """Entidades
1 - GÊNERO DO FILME
"""

MENU_CONTINUE = """Deseja continuar:
1 - SIM
2 - NÃO
"""


# Consulta de contagem de registros por tabela
QUERY_COUNT = 'select count(1) as total_{tabela} from {tabela}'

def clear_console(wait_time:int=6):
    '''
       Esse método limpa a tela após alguns segundos
       wait_time: argumento de entrada que indica o tempo de espera
    '''
    import os
    from time import sleep
    sleep(wait_time)
    os.system("clear")