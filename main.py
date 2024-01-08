# main.py
from time import time  
from fastapi import FastAPI,__version__
from routers.users_db import router as user_router

app = FastAPI() # This is what will be refrenced in config

app.include_router(user_router)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get('/ping')
async def hello():
    return {'res': 'pong', 'version': __version__, "time": time()}