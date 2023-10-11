from model.movie import Movie
from conexion.oracle_queries import OracleQueries

class Controller_Movie:
    def __init__(self):
        pass

    def insert_movie(self) -> Movie:
       
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        movieTypeId = input("Informe o id do gênero de filme: ")

        if not self.verify_movie_type(oracle, movieTypeId):
            movieName = input("Informe o nome do filme: ") 
            movieDescription = input("Informe a descrição do filme: ") 
            moviePriece = input("Informe o preço do produto: ")

            oracle.write(f"insert into LABDATABASE.MOVIE values (MOVIE_ID_SEQ.NEXTVAL, {movieTypeId}, '{movieName}', '{movieDescription}', {moviePriece})")
            df_movie = oracle.sqlToDataFrame(f"select MOVIE_ID, MOVIE_TYPE_ID, movie_name, movie_description, movie_price  from LABDATABASE.MOVIE where MOVIE_NAME = '{movieName}'")

            novo_movie_type = Movie(df_movie.movie_id.values[0], df_movie.movie_type_id.values[0], df_movie.movie_name.values[0], df_movie.movie_description.values[0], df_movie.movie_description.values[0])
            print(novo_movie_type.to_string()) 
            i = input("mawd")
            return novo_movie_type
        else:
            print("O id inserido não existe")
            return None

    def verify_movie_type(self, oracle:OracleQueries, movie_type_id:int=None) -> bool:

        df_movie_type = oracle.sqlToDataFrame(f"select MOVIE_TYPE_ID, MOVIE_TYPE_NAME from LABDATABASE.MOVIE_TYPE where MOVIE_TYPE_ID = {movie_type_id}")
        return df_movie_type.empty