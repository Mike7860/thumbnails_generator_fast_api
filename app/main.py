import crud
import models
import schemas
from database import SessionLocal, engine
from typing import List
from fastapi import Depends, FastAPI, HTTPException, File, UploadFile
from sqlalchemy.orm import Session
from fastapi.openapi.utils import get_openapi


from pathlib import Path
from PIL import Image, ImageFilter
import random
import shutil
import os

from pydantic import BaseModel
from fastapi.responses import HTMLResponse, FileResponse

models.Base.metadata.create_all(bind=engine)
app = FastAPI(debug=True)

base_dir = os.getcwd()
dir_up = str(Path(base_dir).parents[0])
media_dir = os.path.join(dir_up, "media")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/images/")
async def create_upload_file(
    file: UploadFile = File(...), db: Session = Depends(get_db)
):
    with open(media_dir+file.filename, "wb") as image:
        shutil.copyfileobj(file.file, image)

   # return crud.create_user_item(db=db, item=file)
    return file.filename


@app.get("/images/")
async def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items


@app.post("/images/{x}x{y}")
async def show_thumbnail(x: int, y: int, db: Session = Depends(get_db)):
    if len(os.listdir(media_dir)) != 0:
        random_image = random.choice([x for x in os.listdir(media_dir) if os.path.isfile(os.path.join(media_dir, x))])
        print("Random file {}...".format(random_image))
        image = Image.open("x.png")
        size = x, y
        img_edit = image.resize(size)
        img_edit.save("new.png", "PNG")
        print(img_edit)
        show = img_edit.show()
    else:
        raise HTTPException(status_code=404, detail="There is no any photos to show")

    return show


@app.get('/images/{x}x{y}')
async def show_thumbnail(x: int, y: int, db: Session = Depends(get_db)):
    #openapi_schema = get_openapi()
    return "dddd"


# @app.get('/images/', response_model=List[schemas.Item])
# def main():
#     content = """
# <body>
# <form action="/images/" enctype="multipart/form-data" method="post">
# <input name="files" type="file" multiple>
# <input type="submit">
# </form>
# </body>
#     """
#     return HTMLResponse(content=content)
#
#


