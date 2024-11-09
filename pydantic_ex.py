from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel
from pydantic import validator
from typing import Optional

#데이터 유효성 검사
class Model(BaseModel):
    a: int
    b: float
    c: str

external_data = {
    'a': 10,
    'b': 0.05,
    'c': '10',
}

print(Model(**external_data))
print(Model(**external_data).dict())


#customize
class User(BaseModel):
    id: int
    name: str
    email: str

    @validator('email')
    def is_valid_email(cls, v):
        if '@' not in v:
            raise ValueError('must contain an "@" symbol')
        return v

invalid_user = User(id=1, name='Jimmy', email='not-an-email')

