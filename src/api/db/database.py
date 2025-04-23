from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase

passwod_engine = create_async_engine('sqlite+aiosqlite:///password.db')

text_in_read_engine = create_async_engine('sqlite+aiosqlite:///text_read.db')
history_read_engine = create_async_engine('sqlite+aiosqlite:///history_read.db')
grammar_read_engine = create_async_engine('sqlite+aiosqlite:///grammar_read.db')


new_session = async_sessionmaker(passwod_engine, expire_on_commit=False)

new_session_TextRead = async_sessionmaker(text_in_read_engine, expire_on_commit=False)
new_session_HistoryRead = async_sessionmaker(history_read_engine, expire_on_commit=False)
new_session_GrammarRead = async_sessionmaker(grammar_read_engine, expire_on_commit=False)



class Base(DeclarativeBase):
    pass

class Base_Text_Rear(DeclarativeBase):
    pass

class Base_History_Rear(DeclarativeBase):
    pass

class Base_Grammar_Rear(DeclarativeBase):
    pass


async def get_session() -> AsyncSession:
    async with new_session() as session:
        yield session



async def get_text_in_read() -> AsyncSession:
    async with new_session_TextRead() as session_text_read:
        yield session_text_read

async def get_history_read() -> AsyncSession:
    async with new_session_HistoryRead() as session_history_read:
        yield session_history_read

async def get_grammar_read() -> AsyncSession:
    async with new_session_GrammarRead() as session_grammar_read:
        yield session_grammar_read




