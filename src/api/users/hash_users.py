from datetime import timedelta
from sqlalchemy.future import select
from src.api.modals.inst_class import PasswodModel
from src.config import get_auth_data
from passlib.context import CryptContext
from src.config import settings
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from datetime import datetime, timezone
from src.api.db.dependences import SessionDep


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


SECRET_KEY = settings.SECRET_KEY

ALGORITHM = settings.ALGORITHM

ACCESS_TOKEN_EXPIRE_MINUTES = settings.ACCESS_TOKEN_EXPIRE_MINUTES

oauth2_T = OAuth2PasswordBearer(tokenUrl="token")

#Создание JWT токена
# {'sub' : чудо_юзер}
def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})

    # Создание токена
    encode_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encode_jwt

async def get_user(session: SessionDep, username: str):
    result = await session.execute(
        select(PasswodModel).where(PasswodModel.user == username)
    )
    return result.scalars().first()  # Возвращает None, если пользователь не найден


#Хэширование пароля
def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

#Проверка хэшированного пароля и пароля без хэширования
#Сначала открытый пароль, потом хэшированный!
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

#Декодирование JWT токена в имя пользователя
async def get_current_user(token: str = Depends(oauth2_T), session: SessionDep = Depends()):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Не получилось подтвердить данные",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = await get_user(session, username=username)
    if user is None:
        raise credentials_exception
    return {'user': username}







