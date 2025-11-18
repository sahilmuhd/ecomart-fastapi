from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class Store(Base):
    __tablename__ = 'stores'

    id = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    owner_id = Column(String, ForeignKey('users.id'), nullable=False)

    owner = relationship("User", back_populates="stores")

    def __repr__(self):
        return f"<Store(id={self.id}, name={self.name}, owner_id={self.owner_id})>"