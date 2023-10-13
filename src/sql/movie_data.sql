SELECT m.movie_id AS Id_Filme, m.movie_name AS Nome_Filme, mt.movie_type_name AS Nome_Genero_Filme, m.movie_description AS Descricao, m.movie_price AS preco
    FROM LABDATABASE.MOVIE m
    LEFT JOIN LABDATABASE.MOVIE_TYPE mt ON MT.movie_type_id = M.movie_type_id
    ORDER BY movie_id