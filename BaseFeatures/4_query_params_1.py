from fastapi import FastAPI
import os
from typing import Optional

# example query: http://127.0.0.1:8000/items/?skip=0&limit=10
app = FastAPI()

fake_items_db = [{"item_name": "ITEM1"},
                 {"item_name": "ITEM2"},
                 {"item_name": "ITEM3"}]


# range query example
@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    # here query the db
    # out of band requests will not throw errors.
    return fake_items_db[skip : skip + limit]


# optional parameter example
@app.get("/books/{book_id}")
async def read_item(book_id: str, q: Optional[str] = None):

    # http://127.0.0.1:8000/books/1?q=history
    if q:
        return {"book_id": book_id, "q": q}

    # http://127.0.0.1:8000/books/1
    return {"book_id": book_id}


# converting the parameter type
@app.get("/jews/{jew_id}")
async def read_item(jew_id: str, q: Optional[str] = None, short: bool = False):
    # here to make short=True the passed string can be:
    # 1, True, true, on, yes
    jew = {"jew_id": jew_id}
    if q:
        jew.update({"q": q})
    if not short:
        jew.update(
            {"description": "This is an amazing jew."}
        )
    # http://127.0.0.1:11111/jews/larry?q=nut&short=true
    # http://127.0.0.1:11111/jews/larry?q=nut
    return jew


if __name__ == '__main__':
    print(f'INFO:     Starting the FASTAPI server...')
    print(f'INFO:     DOCS on: http://127.0.0.1:11111/docs')
    os.system(f"uvicorn {(__file__.split('/')[-1]).split('.')[0]}:app --host 127.0.0.1 --port 11111")
