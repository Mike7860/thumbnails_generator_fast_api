from sqlalchemy.orm import Session

from . import models, schemas


def get_image(db: Session, id: int):
    return db.query(models.Image).filter(models.Image.id == id).first()


def create_image_item(db: Session, item: schemas.ItemCreate, id: int):
    db_item = models.Image(**item.dict(), owner_id=id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item