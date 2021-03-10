from typing import Optional
import os
from fastapi import FastAPI

app = FastAPI()


# multiple path parameters.
@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int,
    item_id: str,
    q: Optional[str] = None,
    short: bool = False
):
    # http://127.0.0.1:11111/users/1/items/bladeoftheruinedking?q=lifesteal&short=no
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item


# required query parameter
@app.get("/items/{item_id}")
async def read_user_item(item_id: str, needy: str):

    # this throws an error saying that the needy query parameter is required
    # http://127.0.0.1:11111/items/1

    # after filling the needy parameter it works.
    # http://127.0.0.1:11111/items/1?needy=filled

    item = {"item_id": item_id, "needy": needy}
    return item

if __name__ == '__main__':
    print(f'INFO:     Starting the FASTAPI server...')
    print(f'INFO:     DOCS on: http://127.0.0.1:11111/docs')
    os.system(f"uvicorn {(__file__.split('/')[-1]).split('.')[0]}:app --host 127.0.0.1 --port 11111")
