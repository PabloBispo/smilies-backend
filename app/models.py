from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Enum, DateTime
from sqlalchemy.orm import relationship

from .database import Base
import enum

from functools import partial

NotNullColumn = partial(Column, nullable=False)

class PrazoViagem(enum.Enum):
    curto = "curto_prazo"
    medio = "medio_prazo"
    longo = "longo_prazo"


class MyEnum(enum.Enum):
    one = 1
    two = 2
    three = 3

class Usuarios(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    phone = Column(String, unique=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("usuarios.id"))

    owner = relationship("User", back_populates="items")


class Viagem(Base):
    __tablename__ = "viagem"

    id = Column(Integer, primary_key=True, index=True)
    nome = NotNullColumn(String, index=True)
    prazo_viagem = Column(Enum(PrazoViagem))
    milhas = Column(Integer)
    destino = Column(String, index=True)
    cep_destino = Column(String(8))

    origem = Column(String, index=True)
    cep_origem = Column(String(8))

    data_ida = NotNullColumn(DateTime)
    data_volta = NotNullColumn(DateTime)

    owner_id = Column(Integer, ForeignKey("usuarios.id"))

    owner = relationship("Usuarios", back_populates="viagem")