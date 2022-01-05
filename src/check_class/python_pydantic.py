import logging
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel
from pydantic import ValidationError


#------------- BaseModel --------------------
class User(BaseModel):
    id: int
    name = "John Doe"
    singnup_ts: Optional[datetime] = None
    friends: List[int] = []


external_data = {
    "id": "123",
    "singnup_ts": "2019-06-01 12:22",
    "friends": [1, 2, "3"],
}
user = User(**external_data)
print(user.id)
print(repr(user.singnup_ts))
print(user.friends)
print(user.dict())


#--------------- ValidationError ---------------
try:
    User(signup_ts = "broken", friends = [1, 2, "not number"])
except ValidationError as e:
    print(e.json())
