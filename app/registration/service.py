from sqlalchemy.orm import session
from app.database import Session
from app.database.user import User
from .model import RegistrationModel
from app.registration.validators.registration_validators import (
    validate_email_unique,
    email_valid,
    confirm_password
    )


class Registration():
    
    def __init__(self, inputs : RegistrationModel):
        self.__inputs = inputs
        self.session = Session()
        
    
    def registration(self):
        
        sql = User(
            first_names = self.__inputs.first_names,
            surname = self.__inputs.surname,
            email = self.__inputs.email,
            password = self.__inputs.password
        )
        
        query = self.session.query(User.email).filter(User.email == self.__inputs.email).all()
        
        if (validate_email_unique(query) 
            and 
            email_valid(self.__inputs.email)
            and
            confirm_password(self.__inputs.password, self.__inputs.confirm_password)
            ) == True:
            
            self.session.add(sql)
            self.session.commit()
            
            return {
                "status": "passed",
                "message": "User successfully registered!"
            }
        else:    
            return {
                "status": "failed",
                "message": "Registration unsuccessful"
            }
      