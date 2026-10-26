from typing import Annotated
from fastapi import Depends
from sqlmodel import Session
from models.models import Papel
from service.papel_service import PapelService
from database.database import get_session

class PapelServiceImpl(PapelService):

    def __init__(self, session: Annotated[Session, Depends(get_session)]):
        self.session = session

    def create_papel(self, papel: Papel):
        self.session.add(papel)
        self.session.commit()
        self.session.refresh(papel)

    def list_papel(self)->list[Papel]:
        return self.session.query(Papel).all()
