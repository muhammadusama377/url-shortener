from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from fastapi.responses import RedirectResponse

from .database import SessionLocal
from .utils import generate_unique_short_code, create_link, get_link
from . import schemas
from .conf import settings


app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/generate", response_model=schemas.LinkResponse)
def generate_short_url(link: schemas.LinkCreate, db: Session = Depends(get_db)):
    short_code = generate_unique_short_code(db)
    link = create_link(db, {"short_code": short_code, **link.model_dump()})
    return {"short_url": f"{settings.host}/{link.short_code}", "url": link.url}


@app.get("/{short_code}")
def redirect(short_code: str, db: Session = Depends(get_db)):
    link = get_link(db, short_code)
    return RedirectResponse(link.url)
