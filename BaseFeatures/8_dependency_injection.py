from typing import Optional
import os
from fastapi import Depends, FastAPI

app = FastAPI()


# inject common parameters in two endpoints using an async function
async def common_parameters(q: Optional[str] = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}


@app.get("/items/")
async def read_items(commons: dict = Depends(common_parameters)):
    # here the function declares that its dependent to those parameters and
    # then after being received the commons can be used to the users preference
    return commons


@app.get("/users/")
# http://127.0.0.1:11111/users/?q=1&skip=0&limit=10
async def read_users(commons: dict = Depends(common_parameters)):
    return commons

if __name__ == '__main__':
    print(f'INFO:     Starting the FASTAPI server...')
    print(f'INFO:     DOCS on: http://127.0.0.1:11111/docs')
    os.system(f"uvicorn {(__file__.split('/')[-1]).split('.')[0]}:app --host 127.0.0.1 --port 11111")
