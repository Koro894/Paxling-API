# from src.api.dependences import SessionDep
# from src.api.schemas.shablon import BookModel
from os import access

from fastapi import APIRouter
from requests.utils import is_ipv4_address
from sqlalchemy.testing.suite.test_reflection import users

from starlette.responses import RedirectResponse, JSONResponse

from src.api.modals.inst_class import PasswodModel
from src.api.modals.shablon import BookUserRegustration, Users_ID, BookINFO, Delete_User, BookAuthUser, BookToken
from src.config import settings
from sqlalchemy.orm import Session
from sqlalchemy.future import select
from fastapi import Depends, HTTPException, status, Request
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
# 'CryptContext' - это то, что будет использоваться для хэширования и проверки паролей.
from passlib.context import CryptContext
from src.api.db.dependences import SessionDep
from src.api.users.hash_users import create_access_token, verify_password, get_current_user
from typing import Dict
from datetime import datetime
from sqlalchemy import or_



router = APIRouter(
    prefix="/users",
    tags=["Добавление и удаление пользователей"]
)

# для получения подобной строки, выполните: $ openssl rand -hex 32
SECRET_KEY = settings.SECRET_KEY
# алгоритм, используемый для подписи JWT-токена
ALGORITHM = settings.ALGORITHM
# срок действия токена JWT-токена
ACCESS_TOKEN_EXPIRE_MINUTES = settings.ACCESS_TOKEN_EXPIRE_MINUTES



#  функция для хэширования пароля, поступающего от пользователя.
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
# `oauth2_scheme` является "вызываемой" и следовательно ее можно
# использовать в зависимости `fastapi.Depends` в функции `get_current_user()`
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
# создаем экземпляр приложения

@router.delete(
    "/delete_user",
    summary="Удаление пользователя из БД",
)
async def delete_user(data: Delete_User, session: SessionDep):
    result = await  session.execute(select(PasswodModel).where(or_(PasswodModel.user == data.user, PasswodModel.id == data.id)))
    user_del = result.scalars().first()
    if not user_del:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Пользователь не существует!")
    await session.delete(user_del)
    await session.commit()
    return HTTPException(status_code=status.HTTP_200_OK, detail="Пользователь удален.")


@router.post(
    "/sign_regustrat",
    response_model=BookINFO,
    summary="Регистрация нового пользователя"
)
async def sign_regustrat(data: BookUserRegustration, session: SessionDep):
    check_user = await session.execute(
        select(PasswodModel).where(PasswodModel.user == data.user)
    )

    user_uskl = check_user.scalars().all()

    # user_uskl = check_user.scalar_one_or_none()
    if user_uskl:
        raise HTTPException(status_code=404, detail="Такой пользователь уже существует")


    user_data = PasswodModel(**data.model_dump())

    if not hasattr(user_data, 'created_at'):
        user_data.created_at = datetime.utcnow()

    session.add(user_data)
    await session.commit()
    await session.refresh(user_data)
    access_token = create_access_token(data={"exp": data.user})

    # return {"access_token": access_token, "id": user_data.id}
    # return {'token': create_access_token({'user': data.user, 'passwode': data.passwode})
    return BookINFO(
        id=user_data.id,
        user=user_data.user,
        token=access_token,
        created_at=user_data.created_at
    )


@router.post(
    "/auth_user",
    summary="Аутентифицирование пользователя и возвращение токена.",
)
async def get_token(data: BookAuthUser, session: SessionDep):
    result = await session.execute(select(PasswodModel).where(PasswodModel.user == data.user))
    userDB = result.scalars().first()

    if not userDB:
        raise HTTPException(status_code=401, detail="Неправильный логин или пароль")

    if not verify_password(data.password, userDB.password ):
        raise HTTPException(status_code=401, detail="Неправильный логин или пароль")

    return JSONResponse(
        content={"exp": create_access_token(data={'sub': data.user}), "id" : userDB.id},
        status_code=200
    )

@router.get('/ip_adres')
async def get_ip_adress(request: Request):
    ip_user = request.client.host
    return {
        'ip_user': ip_user,
    }


@router.post('/auth_jwt')
async def get_user(data: BookToken, session: SessionDep):
    decod_user = await get_current_user(token=data.token, session=session)
    result = await session.execute(select(PasswodModel).where(PasswodModel.user == decod_user['user']))
    user = result.scalars().first()
    if user:
        return user
    else:
        raise HTTPException(status_code=404, detail="User not found")


