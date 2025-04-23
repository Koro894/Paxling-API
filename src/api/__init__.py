from fastapi import APIRouter

from src.api.texts.ruch_text import router as rut_text
from src.api.users.ruch_users import router as rut_users

main_rut = APIRouter()



main_rut.include_router(rut_text)
main_rut.include_router(rut_users)