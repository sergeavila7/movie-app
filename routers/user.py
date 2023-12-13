from fastapi import APIRouter
from fastapi.responses import HTMLResponse, JSONResponse
from utils.jwt_manager import create_token
from schemas.user import User

user_router = APIRouter()

@user_router.get('/', tags=['home'])
def message():
    return HTMLResponse('<h1>Hello world</h1>')

@user_router.post('/login', tags=['auth'])
def login(user: User):
    if user.email == "admin@gmail.com" and user.password == "admin":
        token: str = create_token(user.model_dump())
        return JSONResponse(status_code=200, content=token)
