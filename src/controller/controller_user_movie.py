from model.user_movie import User_movie
from conexion.oracle_queries import OracleQueries

class Controller_User_movie:
    def __init__(self):
        pass
        
    def insert_sale(self) -> User_movie:
        
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        user_id = input("insira o id do usuário comprador")

        if not self.verifica_existencia_user_byId(oracle, user_id):
            
            movie_id = input("insira o id do filme que deseja comprar")
            
            if not self.verifica_existencia_movie(oracle, movie_id):
                movie_priece = oracle.sqlToDataFrame(f"select movie_price from LABDATABASE.MOVIE where movie_id = {movie_id}")

                i = movie_priece.movie_price.values[0]
                
                oracle.write(f"insert into LABDATABASE.user_movie values (USER_MOVIE_ID_SEQ.NEXTVAL, {user_id}, {movie_id}, {i})")



                df_user_movie = oracle.sqlToDataFrame(f"select user_movie_id, user_id, movie_id, movie_price from LABDATABASE.user_movie where user_movie_id = '{movie_id}'")
                novo_user_movie = User_movie(df_user_movie.user_movie_id.values[0], df_user_movie.user_id.values[0], df_user_movie.movie_id.values[0], df_user_movie.movie_price.values[0])           
                print(novo_user_movie.to_string())
                return novo_user_movie
           
            else:
               print("O id não existe")
               return None

        else:
            print(f"O id não existe.")
            return None
        



    def verifica_existencia_user_byId(self, oracle:OracleQueries, user_id:int=None) -> bool:
        df_user= oracle.sqlToDataFrame(f"select user_id, user_fullname, cpf from LABDATABASE.users where user_id = {user_id}")
        return df_user.empty
    

    def verifica_existencia_movie(self, oracle:OracleQueries, movie_id:int=None) -> bool:
        df_movie= oracle.sqlToDataFrame(f"select movie_id, movie_name from LABDATABASE.movie where movie_id = {movie_id}")
        return df_movie.empty