# import smtplib
# import os
# from email.mime.text import MIMEText
#
# def send_mail(message):
#     sender = "paxling.com"
#     password = "egtac9be58jd93aafl3g"
#
#     server = smtplib.SMTP('smtp.mail.com', 587)
#     server.starttls()
#
#     try:
#         server.login(sender, password)
#         msg = MIMEText(message)
#         server.sendmail(sender, "tabakaev09@mail.ru", msg.as_string())
#
#         return f"Сообщение отправлено!"
#     except Exception as e:
#         return f"Ошибка : {e}"
# def main():
#     message = input()
#     print(send_mail(message))
#
# if __name__ == '__main__':
#     main()
#
#
# # import smtplib
# # from email.mime.text import MIMEText
# # from email.mime.multipart import MIMEMultipart
# #
# # # Настройки SMTP-сервера IHC
# # smtp_server = "p789315.mail.ihc.ru"  # Замените на ваш SMTP-сервер
# # smtp_port = 465  # Порт для SSL
# # login = "admin@пакслинг.рф"  # Ваш полный адрес электронной почты
# # password = "z3b6N9x5An"  # Пароль от почтового ящика
# #
# # # Настройки письма
# # sender_email = login  # Отправитель (ваш адрес)
# # receiver_email = "tabakaev09@mail.ru"  # Получатель
# # subject = "Пример отправки письма"
# # body = "Это тестовое письмо, отправленное с помощью Python."
# #
# # # Создание MIME-сообщения
# # message = MIMEMultipart()
# # message["From"] = sender_email
# # message["To"] = receiver_email
# # message["Subject"] = subject
# #
# # # Добавление текста в тело письма
# # message.attach(MIMEText(body, "plain", "utf-8"))  # Используйте 'utf-8' для кодировки
# #
# # # Установка соединения и отправка письма
# # try:
# #     # Создаем безопасное SSL-соединение с сервером
# #     with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
# #         server.login(login, password)  # Авторизация на сервере
# #         message.as_string().encode('utf-8').decode('utf-8')  # Отправка письма
# #     print("Письмо успешно отправлено!")
# # except Exception as e:
# #     print(f"Ошибка при отправке письма: {e}")
# #
# #
# #
# #
#
#
#
# # import uvicorn
# # from fastapi import FastAPI, BackgroundTasks
# # from fastapi_mail import FastMail, MessageSchema
# #
# #
# # # Настройки электронной почты
# # conf = {
# #     "MAIL_USERNAME": "admin@пакслинг.рф",
# #     "MAIL_PASSWORD": "z3b6N9x5An",  # Введите пароль от почты
# #     "MAIL_FROM": "admin@пакслинг.рф",
# #     "MAIL_PORT": 587,
# #     "MAIL_SERVER": "p789315.mail.ihc.ru",  # Используйте правильный SMTP-сервер
# #     "MAIL_TLS": True,
# #     "MAIL_SSL": False
# # }
# #
# # # Создание приложения FastAPI
# # app = FastAPI()
# #
# # # Экземпляр FastMail
# # fm = FastMail(conf)
# #
# # # Адрес получателя
# # email_to = "tabakaev09@mail.ru"  # Введите адрес получателя
# #
# # # Шаблон сообщения
# # message = MessageSchema(
# #     subject="Простое письмо",
# #     recipients=[email_to],
# #     body="Привет, это тестовое письмо.",
# #     subtype="plain"
# # )
# #
# # # Функция для отправки электронной почты в фоновом режиме
# # def send_email(message: MessageSchema):
# #     fm.send_message(message)
# #
# # # Эндпоинт для отправки электронной почты
# # @app.post("/send-email")
# # async def send_email_endpoint(background_tasks: BackgroundTasks):
# #     background_tasks.add_task(send_email, message)
# #     return {"message": "Письмо отправленоg"}
# #
# # # Тестовый запуск
# # if __name__ == "__main__":
# #     uvicorn.run("src.api.get_in_mail.main:app", reload=True, port=8005)
#
#
#
