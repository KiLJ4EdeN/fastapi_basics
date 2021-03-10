from typing import Optional, List
import os
from fastapi import FastAPI, Query

app = FastAPI()


# query validation in fast api using the Query class.
@app.get("/items/")
async def read_items(q: Optional[str] = Query(None, min_length=3, max_length=50)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


# query with regex
@app.get("/books/")
async def read_items(
    q: Optional[str] = Query(None, min_length=3, max_length=50, regex="^fixedquery$")
):
    results = {"items": [{"book_id": "Foo"}, {"book_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


# make the query a required parameter with "..." as the first argument
@app.get("/nuts/")
async def read_items(q: str = Query(..., min_length=3)):
    results = {"nuts": [{"nut_id": "Foo"}, {"nut_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


# list of items
@app.get("/bags/")
async def read_items(q: Optional[List[str]] = Query(None)):
    # http://127.0.0.1:11111/bags/?q=1&q=2&q=3
    query_items = {"q": q}
    return query_items


@app.get("/numbers/")
async def read_items(q: int = Query(..., lt=150, gt=125)):
    results = {"numbers": [{"number_id": "Foo"}, {"number_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


if __name__ == '__main__':
    print(f'INFO:     Starting the FASTAPI server...')
    print(f'INFO:     DOCS on: http://127.0.0.1:11111/docs')
    os.system(f"uvicorn {(__file__.split('/')[-1]).split('.')[0]}:app --host 127.0.0.1 --port 11111")
