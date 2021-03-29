from sqlalchemy.orm import Session

from . import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.Usuarios).filter(models.Usuarios.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.Usuarios).filter(models.Usuarios.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Usuarios).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password
    db_user = models.Usuarios(
        email = user.email,
        phone = user.phone,
        hashed_password=fake_hashed_password
        )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user



def get_viagens(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Viagem).offset(skip).limit(limit).all()
    

def create_user_viagem(db: Session, viagem: schemas.ViagemCreate, user_id: int):
    db_viagem = models.Viagem(**viagem.dict(), owner_id=user_id)
    db.add(db_viagem)
    db.commit()
    db.refresh(db_viagem)
    return db_viagem