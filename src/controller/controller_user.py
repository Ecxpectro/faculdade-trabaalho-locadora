from model.users import User
from conexion.oracle_queries import OracleQueries

class Controller_User:
    def _init_(self):
        pass
        
    def inserir_user(self) -> User:
        
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        cpf = input("CPF (Novo): ")

        if self.verifica_existencia_user_byId(oracle, cpf):
            
            user_fullname = input("Nome (Novo): ")
            phone = input("phone (Novo): ")
            user_email = input("email    (Novo): ")
            
            oracle.write(f"insert into LABDATABASE.users values (USER_ID_SEQ.NEXTVAL, '{user_fullname}', '{cpf}', '{phone}', '{user_email}' )")
            
            df_user= oracle.sqlToDataFrame(f"select user_id, cpf, user_fullname, phone, user_email  from LABDATABASE.users where cpf = '{cpf}'")
            novo_user = User(df_user.user_id.values[0], df_user.cpf.values[0], df_user.user_fullname.values[0], df_user.phone.values[0], df_user.user_email.values[0])
          
           
            print(novo_user.to_string())
            return novo_user
        else:
            print(f"O CPF {cpf} já está cadastrado.")
            return None


    
    def atualizar_user(self) -> User:
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        update_user = int(input("Digite o id do usuário que deseja alterar"))
        

        if not self.verifica_existencia_user_byId(oracle, update_user): 
          
           new_name = str(input("Digite um novo nome: "))
           new_phone = str(input("Digite um novo telefone: "))
           new_email = str(input("Digite um novo email: "))
           new_cpf = str(input("Digiteum novo CPF: "))

           oracle.write(f"update LABDATABASE.users set phone = '{new_phone}', user_fullname = '{new_name}', user_email = '{new_email}', cpf = '{new_cpf}'  where user_id = {update_user}")

           df_user= oracle.sqlToDataFrame(f"select cpf, user_fullname, phone, user_email  from LABDATABASE.users where cpf = '{new_cpf}'")
           novo_user = User(df_user.cpf.values[0], df_user.user_fullname.values[0], df_user.phone.values[0], df_user.user_email.values[0])

           print(novo_user.to_string())
           return novo_user
    
        else:
            print(f"O id não foi encontrado")
            return None

    

    def verifica_existencia_user(self, oracle:OracleQueries, cpf:str=None) -> bool:
        df_user= oracle.sqlToDataFrame(f"select user_fullname, cpf from LABDATABASE.users where cpf = {cpf}")
        return df_user.empty
    

    def verifica_existencia_user_byId(self, oracle:OracleQueries, user_id:int=None) -> bool:
        df_user= oracle.sqlToDataFrame(f"select user_id, user_fullname, cpf from LABDATABASE.users where user_id = {user_id}")
        return df_user.empty