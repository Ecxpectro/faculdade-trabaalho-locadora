# Exemplo de Sistema em Python fazendo CRUD no Oracle

Esse sistema de exemplo é composto por um conjunto de tabelas que representam pedidos de vendas de filmes, contendo tabelas como: users, movie_type, movie e user_movie.

O sistema exige que as tabelas existam, então basta executar o script Python a seguir para criação das tabelas e preenchimento de dados de exemplos:
```shell
~$ python create_tables_and_records.py
```

Para executar o sistema basta executar o script Python a seguir:
```shell
~$ python principal.py
```

Para que possa testar as conexões com o banco de dados Oracle e o módulo Conexion desenvolvido para esse projeto, basta executar o script Python a seguir:
```shell
~$ python test.py
```

## Organização
- [diagrams](diagrams): Nesse diretório está o [diagrama relacional](diagrams/DIAGRAMA_RELACIONAL_LOCADORA.pdf) (lógico) do sistema.
    * O sistema possui quatro entidades: USERS, MOVIE_TYPE, MOVIE E USER_MOVIE
- [sql](sql): Nesse diretório estão os scripts para criação das tabelas e inserção de dados fictícios para testes do sistema
    * Certifique-se de que o usuário do banco possui todos os privilégios antes de executar os scripts de criação, caso ocorra erro, execute o comando a seguir com o superusuário via SQL Developer: `GRANT ALL PRIVILEGES TO LABDATABASE;`
    * [create_tables_pedidos.sql](sql/create_tables_pedidos.sql): script responsável pela criação das tabelas, relacionamentos e criação de permissão no esquema LabDatabase.
    * [inserting_samples_records.sql](sql/inserting_samples_records.sql): script responsável pela inserção dos registros fictícios para testes do sistema.

- [src](src): Nesse diretório estão os scripts do sistema
    * [conexion](src/conexion): Nesse repositório encontra-se o [módulo de conexão com o banco de dados Oracle](src/conexion/oracle_queries.py). Esse módulo possui algumas funcionalidades úteis para execução de instruções DML e DDL, sendo possível obter JSON, Matriz e Pandas DataFrame.
      - Exemplo de utilização para consultas simples:

        ```python
        def movie_type_data(self, oracle:OracleQueries, need_connect:bool=False):
            query = """
                    select 
                     mt.MOVIE_TYPE_ID AS Id_genero_filme, 
                     mt.MOVIE_TYPE_NAME AS Nome_Genero 
                     from LABDATABASE.MOVIE_TYPE mt
                     order by mt.MOVIE_TYPE_ID
                    """
            if need_connect:
                oracle.connect()
            print(oracle.sqlToDataFrame(query))
        ```
      - Exemplo de utilização para alteração de registros

        ```python
        from model.users import User
        from conexion.oracle_queries import OracleQueries

        class Controller_User:
          def _init_(self):
             pass
        
          def inserir_user(self) -> User:
        
             oracle = OracleQueries(can_write=True)
             oracle.connect()

             cpf = input("CPF (Novo): ")

             if self.verify_user_existence_by_cpf(oracle, cpf):          
                  user_fullname = input("Digite o nome do usuário: ")
                  phone = input("Digite o telefone do usuário: ")
                  user_email = input("Digite o email do usuário: ")
            
                  oracle.write(f"insert into LABDATABASE.users values (USER_ID_SEQ.NEXTVAL, '{user_fullname}', '{cpf}', '{phone}', '{user_email}' )")
            
                  df_user= oracle.sqlToDataFrame(f"select user_id, cpf, user_fullname, phone, user_email  from LABDATABASE.users where cpf = '{cpf}'")
                  novo_user = User(df_user.user_id.values[0], df_user.cpf.values[0], df_user.user_fullname.values[0], df_user.phone.values[0], df_user.user_email.values[0])
          
                  print(novo_user.to_string())
                  return novo_user
             else:
                  print(f"O CPF {cpf} já está cadastrado.")
                  return None
        ```
      - Outros exemplos: [test.py](src/test.py)
      - Caso esteja utilizando na máquina virtual antiga, você precisará alterar o método connect de:
          ```python
          self.conn = cx_Oracle.connect(user=self.user,
                                  password=self.passwd,
                                  dsn=self.connectionString()
                                  )
          ```
        Para:
          ```python
          self.conn = cx_Oracle.connect(user=self.user,
                                  password=self.passwd,
                                  dsn=self.connectionString(in_container=True)
                                  )
          ```
    * [controller](src/controller/): Nesse diretório encontram-sem as classes controladoras, responsáveis por realizar inserção, alteração e exclusão dos registros das tabelas.
    * [model](src/model/): Nesse diretório encontram-ser as classes das entidades descritas no [diagrama relacional](diagrams/DIAGRAMA_RELACIONAL_PEDIDOS.pdf)
    * [reports](src/reports/) Nesse diretório encontra-se a [classe](src/reports/relatorios.py) responsável por gerar todos os relatórios do sistema
    * [sql](src/sql/): Nesse diretório encontram-se os scripts utilizados para geração dos relatórios a partir da [classe relatorios](src/reports/relatorios.py)
    * [utils](src/utils/): Nesse diretório encontram-se scripts de [configuração](src/utils/config.py) e automatização da [tela de informações iniciais](src/utils/splash_screen.py)
    * [create_tables_and_records.py](src/create_tables_and_records.py): Script responsável por criar as tabelas e registros fictícios. Esse script deve ser executado antes do script [principal.py](src/principal.py) para gerar as tabelas, caso não execute os scripts diretamente no SQL Developer ou em alguma outra IDE de acesso ao Banco de Dados.
    * [principal.py](src/principal.py): Script responsável por ser a interface entre o usuário e os módulos de acesso ao Banco de Dados. Deve ser executado após a criação das tabelas.

### Bibliotecas Utilizadas
- [requirements.txt](src/requirements.txt): `pip install -r requirements.txt`

#### Em caso de problemas com a execução dos software dando a seguinte mensagem `ORA-28001: the password has expired`, execute as linhas de comando a seguir no Oracle:
- `ALTER PROFILE DEFAULT LIMIT PASSWORD_LIFE_TIME UNLIMITED;`
- `ALTER USER labdatabase IDENTIFIED BY "labDatabase2022";`
- `ALTER USER labdatabase IDENTIFIED BY  "labDatabase2022";`

### Instalando Oracle InstantClient
- Baixe a versão do [InstantClient](https://www.oracle.com/database/technologies/instant-client/linux-x86-64-downloads.html) de acordo com a versão do Banco de Dados
- Caso esteja utilizando uma distribuição Linux baseado em Debian, será necessário executar o comando a seguir para converter o arquivo .rpm para .deb.
  ```shell
  sudo alien --scripts oracle-instantclient18.5-basic-18.5.0.0.0-3.x86_64.rpm
  ```
- Descompacte o arquivo e será gerado um diretório em um diretório de fácil acesso.
- Mova os diretórios lib e share para dentro do diretório do InstantClient
  ```shell
  sudo mv lib /usr/local/oracle/instantclient_18_5/
  ```
  
  ```shell
  sudo mv share instantclient_18_5/
  ```
- Edite o arquivo `.bash_profile` incluindo as linhas a seguir ao final do arquivo:
  ```shell
  export ORACLE_HOME=/usr/local/oracle/instantclient_18_5/lib/oracle/18.5/client64
  export LD_LIBRARY_PATH=$ORACLE_HOME/lib
  export PATH=$PATH:$ORACLE_HOME/bin
  export PATH
  ```

## Contato
- [LinkedIn](https://www.linkedin.com/in/henrique-schraiber/)
- [E-Mail](mailto:henriquescunha12345@gmail.com)
