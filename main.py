from fastapi import FastAPI, HTTPException, status
import uvicorn
from core.database import get_db
from core import schemas
from core.schemas import createTable
from core.models import UserModel, ResUserModel

app = FastAPI()

dbr = get_db()
createTable()

@app.get("/")
async def root():
    return {"messege":"empr is working fine !"}


@app.get("/users")
async def get_users():
    users = dbr.query(schemas.User).all()
    return {"messege":f"{len(users)} users found !","data":users}

@app.post("/create")
async def create_user(user: UserModel):
    # print(user.model_dump())
    new_user = schemas.User(name=user.name, email = user.email, password = user.password)
    dbr.add(new_user)
    dbr.commit()
    dbr.refresh(new_user)
    return {"messege":"New record inserted !","details":new_user}



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=2004, log_level="info")
