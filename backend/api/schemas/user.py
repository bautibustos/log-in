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