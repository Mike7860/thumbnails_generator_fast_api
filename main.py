from typing import List
#from io import BytesIO
from fastapi import Depends, FastAPI, HTTPException, File, UploadFile
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

from pydantic import BaseModel
from fastapi.responses import HTMLResponse, FileResponse
import shutil

models.Base.metadata.create_all(bind=engine)
app = FastAPI(debug=True)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# class Image(BaseModel):
#     id: int
#     name: str
#     # x_resolution: int
#     # y_resolution: int


@app.get('/images/{x}x{y}')
def show_thumbnail(db: Session = Depends(get_db)):
    return "FileResponse(x)"


@app.post('/images/{x}x{y}')
def show_thumbnail(db: Session = Depends(get_db)):
    image = BytesIO()
    return crud.create_image_item(db=db, item=item, id=id())


@app.get('/images/', response_model=List[schemas.Item])
def main():
    content = """
<body>
<form action="/images/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)


@app.post("/images/", response_model=schemas.Item)
#async def create_upload_file(file: UploadFile = File(...)):
async def create_upload_file(id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)):
    #return {"filename": file.filename}
    return crud.create_image_item(db, item=item, id=id)



