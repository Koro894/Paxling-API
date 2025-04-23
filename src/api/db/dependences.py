from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.api.db.database import get_session, get_text_in_read, get_grammar_read, get_history_read

SessionDep = Annotated[AsyncSession, Depends(get_session)]
SessionDep_Text_in_Read = Annotated[AsyncSession, Depends(get_text_in_read)]
SessionDep_History_in_Read = Annotated[AsyncSession, Depends(get_history_read)]
SessionDep_Grammar_in_Read = Annotated[AsyncSession, Depends(get_grammar_read)]

