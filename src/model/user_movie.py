class User_movie:
    def __init__(self,
                 user_movie_id:str=None,
                 user_id:str=None,
                 movie_id:str=None,
                 movie_price:str=None
                ):
        self.set_user_movie_id(user_movie_id)
        self.set_user_id(user_id)
        self.set_movie_id(movie_id)
        self.set_movie_price(movie_price)


    def set_user_movie_id(self, user_movie_id:str):
        self.user_movie_id  = user_movie_id
    
    def set_user_id(self, user_id:str):
        self.user_id  = user_id
    
    def set_movie_id(self, movie_id:str):
        self.movie_id  = movie_id 

    def set_movie_price(self, movie_price:str):
        self.movie_price  = movie_price
    
    

    def get_user_movie_id(self) -> str:
        return self.user_movie_id

    def get_user_id(self) -> str:
        return self.user_id    
    
    def get_movie_id(self) -> str:
        return self.movie_id    

    def get_movie_price(self) -> str:
        return self.movie_price    
    
    def to_string(self) -> str:
        return f"Venda realizada com exito: "