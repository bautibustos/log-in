from datetime import datetime
from pydantic import BaseModel


class User(BaseModel):
	id_user: int
	name: str
	email: str
	pwd: str

class LoginRequest(BaseModel):
    email: str
    password: str

	# verificacion del mail para generar otp
class OTPrequest(BaseModel):
    email: str

class OTPVerify(BaseModel):
    #se utiliza para buscar en el diccionario
	email: str
	code: int 
    
class UpdatePassword(BaseModel):
	email: str
	pwd: str