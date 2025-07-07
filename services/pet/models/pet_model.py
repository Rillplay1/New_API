from pydantic import BaseModel

class PetModel(BaseModel):

    id: int
    name: str
    status: str

