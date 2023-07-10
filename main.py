from datetime import datetime
from enum import Enum
from typing import List, Optional

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(
    title="Trading App"
)

fake_users = [
    {'id': 1, 'role': 'admin', 'name': 'Max'},
    {'id': 2, 'role': 'user', 'name': 'Vanya'},
    {'id': 3, 'role': 'user', 'name': 'Irina', 'degree': [
        {'id': 1, 'created_at': '2020-01-01T00:00:00', 'type_degree': 'expert'}
    ]},
]


class DegreeType(Enum):
    newbie = "newbie"
    expert = "expert"


class Degree(BaseModel):
    id: int
    created_at: datetime
    type_degree: DegreeType


class User(BaseModel):
    id: int
    role: str
    name: str
    degree: Optional[List[Degree]] # optional означает вернуть null если нет у юзера degree


@app.get("/users/{user_id}", response_model=List[User]) #Валидация отдаваемых данных
def hello(user_id: int):
    return [user for user in fake_users if user['id'] == user_id]



class Trades(BaseModel):
    id: int
    user_id: int
    currency: str = Field(max_length=5) # Максимальное кол-во символов 5
    price: float = Field(ge=0) # Указал вылидацию цены что бы она была больше 0
    amount: float


fake_trades = [
    {'id': 1, 'user_id': '1', 'currency': 'BTC', 'price': 30250, 'amount': 2},
    {'id': 2, 'user_id': '2', 'currency': 'ETC', 'price': 3150, 'amount': 9},
]


@app.post("/trades")   #Валидация данных с помошью класса которые отправляет пользователь на сайт
def get_trades(trades: List[Trades]):
    fake_trades.extend(trades)
    return {'status': 200, 'data': fake_trades}


@app.post("/users/{user_id}")
def hello(user_id: int, name: str):
    current_user = [user for user in fake_users if user['id'] == user_id]
    current_user[0]['name'] = name
    return {'status': 200, 'data': current_user}
