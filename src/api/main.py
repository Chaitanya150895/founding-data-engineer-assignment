"""
main.py
FastAPI app entrypoint
"""
from fastapi import FastAPI
from .routes import router

app = FastAPI(title="Founding Data Engineer Assignment")
app.include_router(router)
