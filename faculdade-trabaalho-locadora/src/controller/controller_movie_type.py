from model.movie_type import MovieType
from conexion.oracle_queries import OracleQueries

class Controller_MovieType:
    def __init__(self):
        pass

    def insert_movie_type(self) -> MovieType:
       
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        
        movieTypeName = input("Informe o novo tipo de filme: ")
 
        oracle.write(f"insert into LABDATABASE.MOVIE_TYPE values (MOVIE_TYPE_ID_SEQ.NEXTVAL, '{movieTypeName}')")
        df_movie_type = oracle.sqlToDataFrame(f"select MOVIE_TYPE_NAME, MOVIE_TYPE_ID from LABDATABASE.MOVIE_TYPE where MOVIE_TYPE_NAME = '{movieTypeName}'")
  
        novo_movie_type = MovieType(df_movie_type.movie_type_name.values[0], df_movie_type.movie_type_id.values[0])
        print(novo_movie_type.to_string())
        return novo_movie_type
    

    def update_movie_type(self) -> MovieType:
        try:
            # Cria uma nova conexão com o banco que permite alteração
            oracle = OracleQueries(can_write=True)
            oracle.connect()

            movie_type_id = int(input("Código do Gênero de filme que irá alterar: "))        

            if not self.verify_movie_type(oracle, movie_type_id):
                new_movie_type_name = input("Nome do Gênero do filme (Novo): ")
                oracle.write(f"update LABDATABASE.MOVIE_TYPE set MOVIE_TYPE_NAME = '{new_movie_type_name}' where MOVIE_TYPE_ID = {movie_type_id}")
                df_movie_type = oracle.sqlToDataFrame(f"select MOVIE_TYPE_ID, MOVIE_TYPE_NAME from LABDATABASE.MOVIE_TYPE where MOVIE_TYPE_ID = {movie_type_id}")

                movie_type_model = MovieType(df_movie_type.movie_type_id.values[0], df_movie_type.movie_type_name.values[0])

                print(movie_type_model.to_string())
                return movie_type_model
            else:
                print(f"O código {movie_type_id} não existe.")
                return None

        except Exception as e:
            print(f"Ocorreu um erro durante a execução: {str(e)}")
            return None

    

    def delete_movie_type(self):
        try:   
            # Cria uma nova conexão com o banco que permite alteração
            oracle = OracleQueries(can_write=True)
            oracle.connect()

            movie_type_id = int(input("Código do Gênero de filme que irá alterar: "))        

            if not self.verify_movie_type(oracle, movie_type_id):            
                df_movie_type = oracle.sqlToDataFrame(f"select MOVIE_TYPE_ID, MOVIE_TYPE_NAME from LABDATABASE.MOVIE_TYPE where MOVIE_TYPE_ID = {movie_type_id}")
                
                # Atualiza a tabela Movie para tirar a associação com o movie_type
                oracle.write(f"update LABDATABASE.MOVIE set MOVIE_TYPE_ID = null where MOVIE_TYPE_ID = {movie_type_id}")            

                oracle.write(f"delete from LABDATABASE.MOVIE_TYPE where MOVIE_TYPE_ID = {movie_type_id}")            
                
                deleted_movie_type = MovieType(df_movie_type.movie_type_id.values[0], df_movie_type.movie_type_name.values[0])
                
                print("Gênero de filme Removido com Sucesso!")
                print(deleted_movie_type.to_string())
            else:
                print(f"O código {movie_type_id} não existe.")
        except Exception as e:
            print(f"Ocorreu um erro durante a execução: {str(e)}")
            return None


    def verify_movie_type(self, oracle:OracleQueries, movie_type_id:int=None) -> bool:

        df_movie_type = oracle.sqlToDataFrame(f"select MOVIE_TYPE_ID, MOVIE_TYPE_NAME from LABDATABASE.MOVIE_TYPE where MOVIE_TYPE_ID = {movie_type_id}")
        return df_movie_type.empty