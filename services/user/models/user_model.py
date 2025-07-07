from pydantic import BaseModel


class UserModel(BaseModel):
    id: int
    username: str
    firstName: str
    lastName: str
    email: str
    password: str
    phone: str
    userStatus: int


# {
#   "id": 0,
#   "username": "string",
#   "firstName": "string",
#   "lastName": "string",
#   "email": "string",
#   "password": "string",
#   "phone": "string",
#   "userStatus": 0
# }