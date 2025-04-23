from datetime import datetime
from optparse import Option
from typing import Any

from click import DateTime
from pandas.core.interchange.dataframe_protocol import Column
from sqlalchemy.dialects.mysql import DATETIME
from typing_extensions import Self, Optional

from pydantic import BaseModel, Field, EmailStr, ConfigDict, field_validator
from src.api.users.hash_users import pwd_context
from src.api.users.hash_users import get_password_hash
from src.yandex_translate.translat import perevod_word
from sqlalchemy import Column, String, func
from sqlalchemy.ext.declarative import declarative_base

class BookAuthUser(BaseModel):
    user: str = Field(..., min_length=5, max_length=100)
    password: str = Field(..., min_length=5, max_length=80)


class BookUserRegustration(BaseModel):
    user: str = Field(..., min_length=5, max_length=100)
    password: str = Field(..., min_length=5, max_length=80)
    description: Optional[str]

    @field_validator('password', mode='before')
    def password_hash(cls, data):
        if data is None:
            raise ValueError('Ошибка, пароль меньше 5 символов или неправильно введен')
        return get_password_hash(data)


class Delete_User(BaseModel):
    id: Optional[int]
    user: Optional[str]

class Delete_Text(BaseModel):
    id: Optional[int]
    title: Optional[str]

class BookToken(BaseModel):
    token: str = Field(...)


class Users_ID(BookUserRegustration):
    id: int
    created_at: datetime

    # nullable - указывает на то, что поле не может быть пустым
    _is_redovui: bool
    _is_researcher: bool
    _is_alchemist: bool
    _is_scientist: bool
    _is_wandering_scientist: bool
    _is_philosopher: bool
    _is_doctor_of_sciences: bool
    _is_wanderer_IT: bool
    _is_doctor_IT: bool
    _is_shadow_site: bool

    _ban: bool

    _right_write_text: bool
    _right_write_comments: bool


    # model_config = ConfigDict(extra='forbid')







class BookModel(BaseModel):
    user: str = Field(..., min_length=5, max_length=40)
    passwode: str = Field(..., min_length=5, max_length=80)
    email: EmailStr
    description: Optional[str] = Field(min_length=0, max_length=1000)




class BookShema(BookModel):
    id: int


class BookText(BaseModel):
    user: str
    before_text: str
    title_text: str



class  BookID(BookText):
    id: int
    created_at: datetime

class Perevod(BaseModel):
    before_text: list
    language: str

class BookINFO(BaseModel):
    id: int
    user: str
    # description: Optional[str]
    token: str
    # _is_redovui: bool
    # _is_researcher: bool
    # _is_alchemist: bool
    # _is_scientist: bool
    # _is_wandering_scientist: bool
    # _is_philosopher:  bool
    # _is_doctor_of_sciences: bool
    # _is_wanderer_IT: bool
    # _is_doctor_IT: bool
    # _is_shadow_site: bool
    created_at: datetime



