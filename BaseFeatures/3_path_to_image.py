from fastapi import FastAPI
import os
import cv2

app = FastAPI()


# end points with dynamic arguments.
@app.get("/images/{image_path:path}")
async def read_item(image_path: str):
    # check if the user started with /
    # else add it to the string.
    # ofc this is only the case with absolute paths.
    if image_path.startswith('/'):
        pass
    else:
        image_path = '/' + image_path
    try:
        image = cv2.imread(image_path)
        return {"image shape": str(image.shape)}
    except AttributeError:
        return {"image shape": "is invalid"}


if __name__ == '__main__':
    print(f'INFO:     Starting the FASTAPI server...')
    print(f'INFO:     DOCS on: http://127.0.0.1:11111/docs')
    os.system(f"uvicorn {(__file__.split('/')[-1]).split('.')[0]}:app --host 127.0.0.1 --port 11111")

