from fastapi import FastAPI, Request
import os

app = FastAPI()


# end points with dynamic arguments.
@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}


# also data types can be used with the endpoint args.
# validation is done for the arg to be an integer here based on the typing information provided.
# ofc the information posted is string but the point is for it to be convertible to int
@app.get("/books/{book_id}")
async def read_books(book_id: int):
    return {"book_id": book_id}


# if wanted to get the clients IP/host.
@app.get("/days/{day_id}")
def read_day(day_id: str, request: Request):
    client_host = request.client.host
    return {"client_host": client_host, "day_id": day_id}


if __name__ == '__main__':
    print(f'INFO:     Starting the FASTAPI server...')
    print(f'INFO:     DOCS on: http://127.0.0.1:11111/docs')
    os.system(f"uvicorn {(__file__.split('/')[-1]).split('.')[0]}:app --host 127.0.0.1 --port 11111")

