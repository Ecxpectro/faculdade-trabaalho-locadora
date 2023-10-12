from model.movie import Movie
from model.users import User
class User_movie:
    def __init__(self,
                 user_movie_id:str=None,
                 user_id:str=None,
                 movie_id:str=None,
                 movie_price:str=None,
                 user_fullname:User=None,
                 movie_name:Movie=None
                ):
        self.set_user_movie_id(user_movie_id)
        self.set_user_id(user_id)
        self.set_movie_id(movie_id)
        self.set_movie_price(movie_price)
        self.set_user_fullname(user_fullname)
        self.set_movie_name(movie_name)

    def set_user_movie_id(self, user_movie_id:str):
        self.user_movie_id  = user_movie_id
    
    def set_user_id(self, user_id:str):
        self.user_id  = user_id
    
    def set_movie_id(self, movie_id:str):
        self.movie_id  = movie_id 

    def set_movie_price(self, movie_price:str):
        self.movie_price  = movie_price
    
    def set_user_fullname(self, user_fullname:User):
        self.user_fullname = user_fullname
    
    def set_movie_name(self, movie_name:Movie):
        self.movie_name = movie_name


    def get_user_movie_id(self) -> str:
        return self.user_movie_id

    def get_user_id(self) -> str:
        return self.user_id    
    
    def get_movie_id(self) -> str:
        return self.movie_id    

    def get_movie_price(self) -> str:
        return self.movie_price    
    
    def get_user_fullname(self) -> User:
        return self.user_fullname
    
    def get_movie_name(self) -> Movie:
        return self.movie_name
    
    def to_string(self) -> str:
        return f"ID: {self.get_user_movie_id()} | Nome do Usuário: {self.get_user_fullname()} | Nome do filme: {self.get_movie_name()} | Preço pago pelo filme: {self.get_movie_price()}"