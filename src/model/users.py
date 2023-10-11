class User:
    def __init__(self, 
                 user_id:str=None,
                 CPF:str=None, 
                 user_fullname:str=None,
                 telefone:str=None,
                 email:str=None
                ):
        self.set_user_id(user_id)
        self.set_CPF(CPF)
        self.set_user_fullname(user_fullname)
        self.set_telefone(telefone)
        self.set_email(email)
        

    def set_user_id(self, user_id:str):
        self.user_id = user_id

    def set_CPF(self, CPF:str):
        self.CPF = CPF

    def set_user_fullname(self, user_fullname:str):
        self.user_fullname = user_fullname

    def set_telefone(self, telefone:str):
        self.telefone = telefone

    def set_email(self, email:str):
        self.email = email

    def get_user_id(self) -> str:
        return self.user_id
    
    def get_CPF(self) -> str:
        return self.CPF

    def get_user_fullname(self) -> str:
        return self.user_fullname

    def get_email(self) -> str:
        return self.email
    
    def get_telefone(self) -> str:
        return self.telefone
    


    def to_string(self) -> str:
        return f"ID: {self.get_user_id()} | CPF: {self.get_CPF()} | user_fullname: {self.get_user_fullname()} Telefone: {self.get_telefone()} Email: {self.get_email()}"