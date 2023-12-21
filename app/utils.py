import shortuuid
from . import models
from sqlalchemy import exists
from sqlalchemy.orm import Session


def generate_short_code():
    return shortuuid.uuid()[:7]


def short_code_exists(db: Session, code):
    ret = db.query(exists().where(models.Link.short_code == code)).scalar()
    return ret


def generate_unique_short_code(db: Session):
    short_code = generate_short_code()
    while short_code_exists(db, short_code):
        short_code = generate_short_code()
    return short_code


def create_link(db: Session, link):
    db_item = models.Link(**link)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def get_link(db: Session, short_code: str):
    return db.query(models.Link).filter(models.Link.short_code == short_code).first()
