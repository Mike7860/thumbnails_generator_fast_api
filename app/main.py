from typing import List
from fastapi import Depends, FastAPI, HTTPException, File, UploadFile
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

import shutil

from pydantic import BaseModel
from fastapi.responses import HTMLResponse, FileResponse

models.Base.metadata.create_all(bind=engine)
app = FastAPI(debug=True)


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
    with open("media/"+file.filename, "wb") as image:
        shutil.copyfileobj(file.file, image)

   # return crud.create_user_item(db=db, item=file)
    return file.filename


@app.get("/images/")
async def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items

@app.get('/images/{x}x{y}')
def show_thumbnail(db: Session = Depends(get_db)):
    return "FileResponse(x)"


@app.post('/images/{x}x{y}')
def show_thumbnail(db: Session = Depends(get_db)):
    return crud.create_image_item(db=db)


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
# @app.post("/images/", response_model=schemas.Item)
# #async def create_upload_file(file: UploadFile = File(...)):
# async def create_upload_file(id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)):
#     #return {"filename": file.filename}
#     return crud.create_image_item(db, item=item, id=id)



