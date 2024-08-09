from typing import Annotated

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.core.db_utils import create_session
from app.core.pydantic_models import TokenPayload, U


reusable_oath2 = OAuth2PasswordBearer(tokenUrl="api_v1/login/access-token")

SessionDep = Annotated[Session, Depends(create_session)]
TokenDep = Annotated[str, Depends(reusable_oath2)]


def get_current_user(session: SessionDep, token: TokenDep):

