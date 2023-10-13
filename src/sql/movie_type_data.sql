select 
mt.MOVIE_TYPE_ID AS Id_genero_filme, 
mt.MOVIE_TYPE_NAME AS Nome_Genero 
from LABDATABASE.MOVIE_TYPE mt
order by mt.MOVIE_TYPE_ID