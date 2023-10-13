SELECT U.user_id AS ID_usuario,
       U.user_fullname AS Nome_Completo,
       U.cpf,
       U.phone AS Telefone,
       U.user_email AS Email,
       UM.Qtd_Filmes_Comprados ,
       UM.Preco_Total_Gasto
FROM LABDATABASE.USERS U
INNER JOIN (
    SELECT user_id, 
           COUNT(DISTINCT user_movie_id) AS Qtd_Filmes_Comprados,
           SUM(movie_total_price) AS Preco_Total_Gasto
    FROM LABDATABASE.USER_MOVIE
    GROUP BY user_id
) UM ON UM.user_id = U.user_id