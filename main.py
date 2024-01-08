# main.py
from time import time  
from fastapi import FastAPI,__version__
from routers.users_db import router as user_router
from fastapi.middleware.cors import CORSMiddleware
from cache_fastapi.cacheMiddleware import CacheMiddleware
app = FastAPI() # This is what will be refrenced in config
origins = ["https://backend-lotr-api-vercel-server.vercel.app/"]
app.include_router(user_router)
cached_endpoints = [
    "/routers/"
]
"""
# Añade el middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Content-Type", "Authorization"],
)
"""
app.add_middleware(CacheMiddleware, cached_endpoints=cached_endpoints)
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get('/ping')
async def hello():
    return {'res': 'pong', 'version': __version__, "time": time()}