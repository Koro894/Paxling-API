from fastapi import FastAPI
from src.api import main_rut
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
# from authx import AuthX, AuthXConfig
#
# config = AuthXConfig()
# config.JWT_SECRET_KEY = "M#it:a_||Hi0922/lo"
# config.JWT_ACCESS_COOKIE_NAME = 'Mila'
# config.JWT_TOKEN_LOCATION = ['cookies']
#
# security = AuthX(config=config)

app = FastAPI()



site_origin = [
    "http://localhost:5173",
    "http://пакслинг.рф",
    "http://127.0.0.1:5173"
]

app.add_middleware(
    CORSMiddleware,
    #в allow_origins надо будет добавить site_origin при развертывании приложения
    allow_origins=site_origin,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(main_rut)

#при сворачивании в dockerfile добавить
# host="0.0.0.0"
if __name__ == "__main__":
    uvicorn.run("src.main:app", reload=True, port=8010)











