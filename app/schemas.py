from typing import List, Dict, Optional
from datetime import datetime

from pydantic import BaseModel
import enum


class PrazoViagem(enum.Enum):
    curto = "curto_prazo"
    medio = "medio_prazo"
    longo = "longo_prazo"


class ViagemBase(BaseModel):
    nome: str
    prazo_viagem: PrazoViagem
    milhas: int
    destino: str
    cep_destino: str

    origem: str
    cep_origem: str

    data_ida: datetime
    data_volta: datetime


class ViagemCreate(ViagemBase):
    ...


class Viagem(ViagemBase):
    id: int
    owner_id: int
    
    class Config:
        orm_mode = True


class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None


class ItemCreate(ItemBase):
    ...


class Item(ItemBase):
    id: int
    owner_id: int
    
    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str
    phone: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []

    class Config:
        orm_mode = True
