from starlette import status
from models.models import Papel
from database.database import get_session
from typing import Annotated
from fastapi import Depends, APIRouter, HTTPException
from routes.login_router import UsuarioLogado
from service.implementation.papel_service_implementation import PapelServiceImpl
from service.papel_service import PapelService

SessionDep = Annotated[get_session, Depends(get_session)]
papel_service = Annotated[PapelService, Depends(PapelServiceImpl)]
router = APIRouter(prefix="/papeis", tags=["papel"])

@router.get("/", response_model=list[Papel])
def get_papel(service: papel_service)->list[Papel]:
    return service.list_papel()

@router.get("/{id}", response_model=Papel)
def get_papel_by_id(id: int, session: SessionDep)->Papel:
    return session.query(Papel).get(id)

@router.post("/", response_model=Papel)
def create_papel(papel: Papel,
                 service: papel_service,
                 usuario:UsuarioLogado)-> Papel:

    service.create_papel(papel)
    return papel

@router.delete("/{id}")
def delete_papel(id: int, session: SessionDep)-> None:
    papel = session.query(Papel).get(id)
    session.delete(papel)
    session.commit()

@router.put("/{id}",response_model=Papel)
def update_papel(id: int, papel: Papel, session: SessionDep)-> Papel:
    papel_db= session.query(Papel).get(id)
    if papel_db is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Papel não encontrado")
    for key, value in papel.model_dump(exclude_unset=True).items():
        setattr(papel_db, key, value)
    session.add(papel_db)
    session.commit()
    session.refresh(papel_db)
    session.commit()
    return papel_db