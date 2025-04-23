import requests
from src.config import settings
import json
from math import ceil



# Параметры для аутентификации с помощью API-ключа от имени сервисного аккаунта:
API_KEY = settings.API_KEY
# Параметры для аутентификации с помощью IAM-токена:
# IAM_TOKEN = '<IAM-токен>'
import re
FOLDER_ID = settings.FOLDER_ID

def define_languages(text: str) -> str:
    pass

def perevod_word(before_text: list, target_language: str) -> dict:
    after_text = []
    for i in before_text:
        i.replace('\n', '\\n')
        after_text.append(i)
    body = {
        "targetLanguageCode": target_language,
        "texts": after_text,
        "folderId": FOLDER_ID,
    }
    headers = {
        "Content-Type": "application/json",
        # Параметры для аутентификации с помощью API-ключа от имени сервисного аккаунта:

        "Authorization": "Api-Key {0}".format(API_KEY),

        # Параметры для аутентификации с помощью IAM-токена:
        # "Authorization": "Bearer {0}".format(IAM_TOKEN)

    }
    response = requests.post(
        "https://translate.api.cloud.yandex.net/translate/v2/translate",
        json=body,
        headers=headers,
    )
    data = response.json()
    data_str = data['translations'][0]['text']
    print(data_str)
    return data_str

def BIG_perevod_word(before_text: str, target_language: str) -> str:
    int_api_run = ceil(len(before_text) / 9000)

    for i in range():
        pass



