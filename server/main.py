from fastapi import FastAPI
from db.database import SessionLocal, engine
from db.models import user

user.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}
