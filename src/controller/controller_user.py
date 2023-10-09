from model.users import User
from conexion.oracle_queries import OracleQueries

class Controller_User:
    def _init_(self):
        pass
        
    def inserir_user(self) -> User:
        ''' Ref.: https://cx-oracle.readthedocs.io/en/latest/user_guide/plsql_execution.html#anonymous-pl-sql-blocks'''
        
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        # Solicita ao usuario o novo CPF
        cpf = input("CPF (Novo): ")

        if self.verifica_existencia_user(oracle, cpf):
            # Solicita ao usuario o novo nome
            user_fullname = input("Nome (Novo): ")
            phone = input("phone (Novo): ")
            user_email = input("email    (Novo): ")
            # Insere e persiste o novo user 
            oracle.write(f"insert into LABDATABASE.users values (USER_ID_SEQ.NEXTVAL, '{user_fullname}', '{cpf}', '{phone}', '{user_email}' )")
            # Recupera os dados do novo usercriado transformando em um DataFrame
            df_user= oracle.sqlToDataFrame(f"select cpf, user_fullname, phone, user_email  from LABDATABASE.users where cpf = '{cpf}'")
            # Cria um novo objeto user
            print("aqui")
            print(df_user.cpf)
            print(df_user.user_fullname)
            print(df_user.phone)
            print(df_user.user_email)
            novo_user = User(df_user.cpf.values[0], df_user.user_fullname.values[0], df_user.phone.values[0], df_user.user_email.values[0])
            # Exibe os atributos do novo user
            print(novo_user.to_string())
            # Retorna o objeto novo_user para utilização posterior, caso necessário
            return novo_user
        else:
            print(f"O CPF {cpf} já está cadastrado.")
            return None

  

    def verifica_existencia_user(self, oracle:OracleQueries, cpf:str=None) -> bool:
        # Recupera os dados do novo usercriado transformando em um DataFrame
        df_user= oracle.sqlToDataFrame(f"select user_fullname, cpf from LABDATABASE.users where cpf = {cpf}")
        return df_user.empty