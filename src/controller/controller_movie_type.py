from model.movie_type import MovieType
from conexion.oracle_queries import OracleQueries

class Controller_MovieType:
    def __init__(self):
        pass

    def inserir_movie_type(self) -> MovieType:
       
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        
        movieTypeName = input("Informe o novo tipo de filme: ")
 
        oracle.write(f"insert into LABDATABASE.MOVIE_TYPE values (MOVIE_TYPE_ID_SEQ.NEXTVAL, '{movieTypeName}')")
        df_movie_type = oracle.sqlToDataFrame(f"select MOVIE_TYPE_NAME, MOVIE_TYPE_ID from LABDATABASE.MOVIE_TYPE where MOVIE_TYPE_NAME = '{movieTypeName}'")
        print(df_movie_type)
        novo_movie_type = MovieType(df_movie_type.movie_type_name.values[0], df_movie_type.movie_type_id.values[0])
        print(novo_movie_type.to_string())
        return novo_movie_type
        