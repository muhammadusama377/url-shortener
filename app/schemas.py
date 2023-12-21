from pydantic import BaseModel, ConfigDict


class LinkBase(BaseModel):
    short_code: str
    url: str
    expired: bool = False


class LinkCreate(BaseModel):
    url: str


class Link(LinkBase):
    model_config = ConfigDict(from_attributes=True)

    id: int


class LinkResponse(BaseModel):
    short_url: str
    url: str
