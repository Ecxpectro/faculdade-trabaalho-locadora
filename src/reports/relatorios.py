from conexion.oracle_queries import OracleQueries

class Relatorio:
    def __init__(self):
       
        with open("sql/relatorio_user_details_data.sql") as f:
            self.query_user_details_data = f.read()

        with open("sql/movie_type_data.sql") as f:
            self.query_movie_type_data = f.read()
        
        with open("sql/user_data.sql") as f:
            self.query_user_data = f.read()
        
        with open("sql/movie_data.sql") as f:
            self.query_movie_data = f.read()
        
        with open("sql/sales_data.sql") as f:
            self.query_sales_data = f.read()

    def get_movie_type_data(self):
        oracle = OracleQueries()
        oracle.connect()
        
        print(oracle.sqlToDataFrame(self.query_movie_type_data))
        input("Pressione Enter para continuar")

    def get_user_data(self):
        oracle = OracleQueries()
        oracle.connect()

        print(oracle.sqlToDataFrame(self.query_user_data))
        input("Pressione Enter para continuar")

    def get_movie_data(self):
        oracle = OracleQueries()
        oracle.connect()

        print(oracle.sqlToDataFrame(self.query_movie_data))
        input("Pressione Enter para continuar")

    def get_relatorio_user(self):
        oracle = OracleQueries()
        oracle.connect()

        print(oracle.sqlToDataFrame(self.query_user_details_data))
        input("Pressione Enter para continuar")
    
    def get_sales_data(self):
        oracle = OracleQueries()
        oracle.connect()

        print(oracle.sqlToDataFrame(self.query_sales_data))
        input("Pressione Enter para continuar")