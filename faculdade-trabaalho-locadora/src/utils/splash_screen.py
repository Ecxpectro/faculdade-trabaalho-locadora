from conexion.oracle_queries import OracleQueries
from utils import config

class SplashScreen:

    def __init__(self):
        # Consultas de contagem de registros - inicio
        self.qry_total_produtos = config.QUERY_COUNT.format(tabela="movie")
        self.qry_total_clientes = config.QUERY_COUNT.format(tabela="users")
        self.qry_total_fornecedores = config.QUERY_COUNT.format(tabela="movie_type")
        self.qry_total_pedidos = config.QUERY_COUNT.format(tabela="user_movie")
        # Consultas de contagem de registros - fim

        # Nome(s) do(s) criador(es)
        self.created_by1 = "Henrique Schraiber Cunha, Guilherme Reis Kill,"
        self.created_by2 = "Rodrigo Kill Correa, Ana Carolina Lopes Dalvi,"
        self.created_by3 = "Ludovico Monjardim, Kevin Dos Reis Hartwig"

        
        self.professor = "Prof. M.Sc. Howard Roatti"
        self.disciplina = "Banco de Dados"
        self.semestre = "2023/2"

    def get_total_movies(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Retorna o total de registros computado pela query
        return oracle.sqlToDataFrame(self.qry_total_produtos)["total_movie"].values[0]

    def get_total_clients(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Retorna o total de registros computado pela query
        return oracle.sqlToDataFrame(self.qry_total_clientes)["total_users"].values[0]

    def get_total_movie_type(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Retorna o total de registros computado pela query
        return oracle.sqlToDataFrame(self.qry_total_fornecedores)["total_movie_type"].values[0]

    def get_total_sales(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Retorna o total de registros computado pela query
        return oracle.sqlToDataFrame(self.qry_total_pedidos)["total_user_movie"].values[0]

    def get_updated_screen(self):
        return f"""
        ########################################################
        #              SISTEMA DE VENDAS DE FILMES                     
        #                                                         
        #  TOTAL DE REGISTROS:                                    
        #      1 - FILMES:               {str(self.get_total_movies()).rjust(5)}
        #      2 - CLIENTES:             {str(self.get_total_clients()).rjust(5)}
        #      3 - GÊNEROS DE FILME:     {str(self.get_total_movie_type()).rjust(5)}
        #      4 - VENDAS:               {str(self.get_total_sales()).rjust(5)}
        #
        #  CRIADO POR: {self.created_by1}
        #              {self.created_by2}
        #              {self.created_by3}
        #
        #  PROFESSOR:  {self.professor}
        #
        #  DISCIPLINA: {self.disciplina}
        #              {self.semestre}
        ########################################################
        """