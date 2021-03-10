from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
import os


# use a pydantic basemodel to define the data schema that has to be posted.
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


app = FastAPI()


@app.put("/items/{item_id}")
async def create_item(item_id: int, item: Item, q: Optional[str] = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result

if __name__ == '__main__':
    print(f'INFO:     Starting the FASTAPI server...')
    print(f'INFO:     DOCS on: http://127.0.0.1:11111/docs')
    os.system(f"uvicorn {(__file__.split('/')[-1]).split('.')[0]}:app --host 127.0.0.1 --port 11111")
