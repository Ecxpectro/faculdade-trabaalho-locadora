SELECT um.user_movie_id AS Ordem_Venda,
u.user_fullname AS Nome_CLiente,
m.movie_name AS Nome_Filme, 
m.movie_description AS Descricao, 
um.movie_total_price AS Valor_Pago
FROM LABDATABASE.USER_MOVIE um
INNER JOIN LABDATABASE.USERS u ON u.user_id = um.user_id
INNER JOIN LABDATABASE.MOVIE m ON m.movie_id = um.movie_id