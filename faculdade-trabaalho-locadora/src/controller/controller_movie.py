from model.movie import Movie
from utils import config
from conexion.oracle_queries import OracleQueries
from reports.relatorios import Relatorio
relatorio = Relatorio()
class Controller_Movie:
    def __init__(self):
        pass

    def insert_movie(self) -> Movie:

        try:  
            oracle = OracleQueries(can_write=True)
            oracle.connect()

            movieTypeId = input("Informe o id do gênero de filme: ")

            if not self.verify_movie(oracle, movieTypeId):
                movieName = input("Informe o nome do filme: ") 
                movieDescription = input("Informe a descrição do filme: ") 
                moviePriece = input("Informe o preço do produto: ")

                oracle.write(f"insert into LABDATABASE.MOVIE values (MOVIE_ID_SEQ.NEXTVAL, {movieTypeId}, '{movieName}', '{movieDescription}', {moviePriece})")
                df_movie = oracle.sqlToDataFrame(f"select MOVIE_ID, MOVIE_TYPE_ID, movie_name, movie_description, movie_price  from LABDATABASE.MOVIE where MOVIE_NAME = '{movieName}'")
                selectGenero = oracle.sqlToDataFrame(f"select movie_type_name from movie_type where movie_type_id = {movieTypeId}")

                novo_movie_type = Movie(df_movie.movie_id.values[0], df_movie.movie_type_id.values[0],selectGenero.movie_type_name.values[0], df_movie.movie_name.values[0], df_movie.movie_description.values[0], df_movie.movie_description.values[0])
                print(novo_movie_type.to_string()) 
                return novo_movie_type
            else:
                print("O id inserido não existe")
                return None
        except Exception as e:
            print(f"Ocorreu um erro durante a execução: {str(e)}")
            return None

    def update_movie(self) -> Movie:
        try:
            oracle = OracleQueries(can_write=True)
            oracle.connect()

            movie_id = int(input("Informe o id do filme que deseja alterar: "))

            if not self.verify_movie_byId(oracle, movie_id):
                config.clear_console()
                relatorio.get_movie_type_data()
                movie_type_id = int(input("infome o id do gênero: "))

                if not self.verify_movie(oracle, movie_type_id):
                    movieName = input("Informe o novo nome: ") 
                    movieDescription = input("Informe a nova descricção: ") 
                    moviePriece = input("Informe o novo preço: ")

                    oracle.write(f"update LABDATABASE.MOVIE set movie_type_id = {movie_type_id}, movie_name = '{movieName}', movie_description = '{movieDescription}', movie_price = '{moviePriece}' where movie_id = {movie_id}")
                    df_movie = oracle.sqlToDataFrame(f"select MOVIE_ID, MOVIE_TYPE_ID, movie_name, movie_description, movie_price  from LABDATABASE.MOVIE where MOVIE_NAME = '{movieName}'")
                    new_genero_name = oracle.sqlToDataFrame(f"select movie_type_name from movie_type where movie_type_id = {movie_type_id}")

                    novo_movie_type = Movie(df_movie.movie_id.values[0], df_movie.movie_type_id.values[0],new_genero_name.movie_type_name.values[0] , df_movie.movie_name.values[0], df_movie.movie_description.values[0], df_movie.movie_description.values[0])
                    print(novo_movie_type.to_string()) 
                    return novo_movie_type
            else:
                print("O id inserido não existe")
                return None
        except Exception as e:
            print(f"Ocorreu um erro durante a execução: {str(e)}")
            return None
    def verify_movie(self, oracle:OracleQueries, movie_type_id:int=None) -> bool:
        df_movie_type = oracle.sqlToDataFrame(f"select MOVIE_TYPE_ID, MOVIE_TYPE_NAME from LABDATABASE.MOVIE_TYPE where MOVIE_TYPE_ID = {movie_type_id}")
        return df_movie_type.empty

    def verify_movie_byId(self, oracle:OracleQueries, movie_id:int=None) -> bool:

        df_movie = oracle.sqlToDataFrame(f"select MOVIE_ID, MOVIE_NAME from LABDATABASE.MOVIE where MOVIE_ID = {movie_id}")
        return df_movie.empty