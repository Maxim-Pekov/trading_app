from fastapi import FastAPI


app = FastAPI(
    title="Trading App"
)

fake_users = [
    {'id': 1, 'role': 'admin', 'name': 'Max'},
    {'id': 2, 'role': 'user', 'name': 'Vanya'}
]

fake_trades = [
    {'id': 1, 'user_id': '1', 'currency': 'BTC', 'price': 30250, 'amount': 2},
    {'id': 2, 'user_id': '2', 'currency': 'ETC', 'price': 3150, 'amount': 9},
]


@app.get("/users/{user_id}")
def hello(user_id: int):
    return [user for user in fake_users if user['id'] == user_id]

@app.get("/trades")
def get_trades(limit: int = 1, offset: int = 0):
    return fake_trades[offset:][:limit]

@app.post("/users/{user_id}")
def hello(user_id: int, name: str):
    current_user = [user for user in fake_users if user['id'] == user_id]
    current_user[0]['name'] = name
    return {'status': 200, 'data': current_user}
