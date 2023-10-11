from fastapi import FastAPI

from .routers import routers

app = FastAPI()

# include routers
app.include_router(routers)
