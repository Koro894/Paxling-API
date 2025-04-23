from sqlalchemy import text, String
from datetime import datetime

# from sqlalchemy import select
# from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import Mapped, mapped_column, declarative_base

# from src.api.texts.ruch_text import text_get
from src.api.db.database import Base, Base_Text_Rear, Base_History_Rear, Base_Grammar_Rear
from sqlalchemy import Column, DateTime, func, Integer, Boolean



class PasswodModel(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user: Mapped[str] = mapped_column(String(100), nullable=False)
    password: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str | None] = mapped_column(String(2000), nullable=True)

    _is_redovui: Mapped[bool] = mapped_column(Boolean, default=True, server_default='true', nullable=False)
    _is_researcher: Mapped[bool] = mapped_column(Boolean, default=False, server_default='false', nullable=False)
    _is_alchemist: Mapped[bool] = mapped_column(Boolean, default=False, server_default='false', nullable=False)
    _is_scientist: Mapped[bool] = mapped_column(Boolean, default=False, server_default='false', nullable=False)
    _is_wandering_scientist: Mapped[bool] = mapped_column(Boolean, default=False, server_default='false', nullable=False)
    _is_philosopher: Mapped[bool] = mapped_column(Boolean, default=False, server_default='false', nullable=False)
    _is_doctor_of_sciences: Mapped[bool] = mapped_column(Boolean, default=False, server_default='false', nullable=False)
    _is_wanderer_IT: Mapped[bool] = mapped_column(Boolean, default=False, server_default='false', nullable=False)
    _is_doctor_IT: Mapped[bool] = mapped_column(Boolean, default=False, server_default='false', nullable=False)
    _is_shadow_site: Mapped[bool] = mapped_column(Boolean, default=False, server_default='false', nullable=False)

    _ban: Mapped[bool] = mapped_column(Boolean, default=False, server_default='false', nullable=False)

    _right_write_text: Mapped[bool] = mapped_column(Boolean, default=False, server_default='false', nullable=False)
    _right_write_comments: Mapped[bool] = mapped_column(Boolean, default=True, server_default='true', nullable=False)

    created_at: Mapped[DateTime] = mapped_column(DateTime, default=func.now())


    # level_aura - уровень пользователя.
    # Будет 12 уровней.
    # 1 - Рядовой
    # 2 - Исследователь
    # 3 - Алхимик
    # 4 - Учёный
    # 5 - Странствующий Учёный
    # 6 - Философ
    # 7 - Доктор наук
    # 8 - Странник IT
    # 9 - Доктор IT
    # 10 -Тень сайта




class PasswodMod_TextRead(Base_Text_Rear):
    __tablename__ = "text_rea"

    id = Column(Integer, primary_key=True)
    user = Column(String)
    title_text = Column(String)
    before_text = Column(String)
    en_text = Column(String)
    created_at = Column(DateTime, default=func.now())  # Значение по умолчанию

class PasswodMod_HistoryRead(Base_History_Rear):
    __tablename__ = "history_read"

    id: Mapped[int] = mapped_column(primary_key=True)
    user: Mapped[str]
    title_text: Mapped[str]
    text: Mapped[str]
    created_at: Mapped[datetime]
    like_post: Mapped[int]

class PasswodMod_GrammarRead(Base_Grammar_Rear):
    __tablename__ = "grammar_read"

    id: Mapped[int] = mapped_column(primary_key=True)
    user: Mapped[str]
    title_text: Mapped[str]
    text: Mapped[str]

