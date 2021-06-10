from pydantic import BaseModel

class RegistrationModel(BaseModel):
    first_names : str
    surname : str
    email : str
    password : str
    confirm_password : str
    