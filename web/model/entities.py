from sqlalchemy import Column, Integer, String, Sequence, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import connector

class Alumno(connector.Manager.Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('codigo_alumno'), primary_key=True)
    nombre = Column(String(20))
    apellido = Column(String(30))
    carrera = Column(String(50))