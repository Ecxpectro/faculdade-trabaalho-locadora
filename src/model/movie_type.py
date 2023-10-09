class MovieType:
    def __init__(self,
                 movie_type_id:str=None,
                 movie_type_name:str=None
                ):
        self.set_movie_type_id(movie_type_id)
        self.set_movie_type_name(movie_type_name)

    def set_movie_type_id(self, movie_type_id:str):
        self.movie_type_id  = movie_type_id   
    
    def set_movie_type_name(self, movie_type_name:str):
        self.movie_type_name  = movie_type_name    
    
    

    def get_movie_type_id(self) -> str:
        return self.movie_type_id
    
    def get_movie_type_name(self) -> str:
        return self.movie_type_name
    
    def to_string(self) -> str:
        return f"Id: {self.get_movie_type_id()} | Nome do gênero de filme: {self.get_movie_type_name()}"