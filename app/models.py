from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Enum, DateTime
from sqlalchemy.orm import relationship

from .database import Base
import enum

from functools import partial

NotNullColumn = partial(Column, nullable=False)

class PrazoViagem(str, enum.Enum):
    curto = 'Curto Prazo'
    medio = 'Médio Prazo'
    longo = 'Longo Prazo'


class Usuarios(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    phone = Column(String, unique=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    viagens = relationship("Viagem", back_populates="owner")


class Viagem(Base):
    __tablename__ = "viagens"

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

    owner = relationship("Usuarios", back_populates="viagens")