from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel
from utils.jwt_manager import create_token
from config.database import engine, Base
from middlewares.error_handler import ErrorHandler
from routers.movie import movie_router
from routers.user import user_router

app = FastAPI()
app.title = "Mi aplicacion con FastAPI"
app.version = "0.0.1"

# Agregar el middleware
app.add_middleware(ErrorHandler)

# Incluir las rutas
app.include_router(user_router)
app.include_router(movie_router)

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)
