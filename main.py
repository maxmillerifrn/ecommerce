from fastapi import FastAPI
from routes import usuario_routes,papel_router,login_router
from contextlib import asynccontextmanager
from database.database import create_db_and_tables
@asynccontextmanager
async def lifespan(app:FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(usuario_routes.router)
app.include_router(papel_router.router)
app.include_router(login_router.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
