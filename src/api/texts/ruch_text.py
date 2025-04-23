from fastapi import APIRouter, Depends, HTTPException
from requests import session
from sqlalchemy.future import select

from src.api.db.dependences import SessionDep_Text_in_Read
from src.api.db.database import *

from src.api.modals.inst_class import PasswodMod_TextRead, PasswodModel
from src.api.modals.shablon import BookText, BookID, Perevod, Delete_Text
from sqlalchemy import Column, DateTime, func
from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime




from src.yandex_translate.translat import perevod_word

router = APIRouter(
    prefix="/text",
    tags=["Добавление и получение большого текста"]
)


@router.post("/setup_database", summary="Загрузка баз данных")
async def setup_database():
    async with passwod_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    async with text_in_read_engine.begin() as conn_text_read:
        await conn_text_read.run_sync(Base_Text_Rear.metadata.create_all)

    async with history_read_engine.begin() as conn_history_read:
        await conn_history_read.run_sync(Base_History_Rear.metadata.create_all)

    async with grammar_read_engine.begin() as conn_grammar_read:
        await conn_grammar_read.run_sync(Base_Grammar_Rear.metadata.create_all)

    return {'ok': True}


@router.post("/text_setup", summary="Добавление текста")
async def add_text(data: BookText, session: SessionDep_Text_in_Read):

    result = await session.execute(
        select(PasswodMod_TextRead).where(PasswodMod_TextRead.title_text == data.title_text)
    )
    except_text = result.scalars().first()

    if except_text:
        await session.rollback()
        raise HTTPException(status_code=404, detail="Текст с таким названием уже существует")

    new_text = PasswodMod_TextRead(**data.model_dump())

    # Добавляет created_at с текущим временем, если его нет в BookText
    if not hasattr(new_text, 'created_at'):
        new_text.created_at = datetime.utcnow()

    if hasattr(new_text, 'en_text'):
        new_text.en_text = perevod_word([new_text.before_text], "en")



    session.add(new_text)
    await session.commit()
    await session.refresh(new_text)



@router.get("/text_get_user", summary="Получение всех авторов текстов для чтения")
async def read_users(db: SessionDep_Text_in_Read):
    text = await db.execute(select(PasswodMod_TextRead.user))
    all_text = text.scalars().all()
    return all_text

@router.get("/text_get_title", summary="Получение всех названий текстов для чтения")
async def read_users(db: SessionDep_Text_in_Read):
    text = await db.execute(select(PasswodMod_TextRead.title_text))
    all_text = text.scalars().all()
    return all_text


@router.get("/text_get_before", summary="Получение всех текстов для чтения")
async def read_users(db: SessionDep_Text_in_Read):
    text = await db.execute(select(PasswodMod_TextRead.before_text))
    all_text = text.scalars().all()
    return all_text

@router.get("/text_get_en", summary="Получение всех текстов по английски для чтения")
async def read_users(db: SessionDep_Text_in_Read):
    text = await db.execute(select(PasswodMod_TextRead.en_text))
    all_text = text.scalars().all()
    return all_text

@router.post('/text_translater', summary="Перевод текста")
async def translate_text(data: Perevod):
    print(data.dict())  # Логирование входящих данных
    perevod = perevod_word(data.before_text, data.language)
    return perevod

@router.delete('/delete_text', summary="Удаление текста")
async def delete_text(data: Delete_Text, db: SessionDep_Text_in_Read):
    pass




