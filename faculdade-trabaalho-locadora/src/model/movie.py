from model.movie_type import MovieType
class Movie:
    def __init__(self,
                 movie_id:str=None,
                 movie_type_id:str=None,
                 movie_genero:str=None,
                 movie_name:str=None,
                 movie_description:str=None,
                 movie_priece:str=None
                ):
        self.set_movie_id(movie_id)
        self.set_movie_type_id(movie_type_id)
        self.set_movie_name(movie_name)
        self.set_movie_description(movie_description)
        self.set_movie_priece(movie_priece)
        self.set_movie_genero(movie_genero)

    def set_movie_genero(self, movie_genero):
        self.movie_genero = movie_genero

    def set_movie_type_id(self, movie_type_id):
        self.movie_type_id = movie_type_id

    def set_movie_id(self, movie_id):
        self.movie_id = movie_id

    def set_movie_name(self, movie_name:str):
        self.movie_name  = movie_name   
    
    def set_movie_description(self, movie_description:str):
        self.movie_description  = movie_description   
    
    def set_movie_priece(self, movie_priece:str):
        self.movie_priece = movie_priece
    
    def get_movie_id(self) -> str:
        return self.movie_id
    
    def get_movie_type_id(self, movie_type_id:str):
        return self.movie_type_id

    def get_name(self) -> str:
        return self.movie_name
    
    def get_movie_genero(self) -> str:
        return self.movie_genero

    def get_movie_description(self) -> str:
        return self.movie_description
    
    def get_movie_priece(self) -> str:
        return self.movie_priece
    
    
    def to_string(self) -> str:
        return f"Nome filme é: {self.get_name()} | O genero do filme é: {self.get_movie_genero()} | A descrição do filme é: {self.get_movie_description()} | O preço do filme é {self.get_movie_priece()}"