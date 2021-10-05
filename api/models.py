from bson import ObjectId
from pydantic import BaseModel, Field
from typing import Optional


class PyObjectId(ObjectId):

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type='string')

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError('Invalid ObjectId')
        return ObjectId(v)


class Thing(BaseModel):
    id: Optional[PyObjectId] = Field(alias='_id')
    name: str
    value: int

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str,
        }
