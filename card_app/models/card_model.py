import sqlalchemy as sa

from datetime import datetime

from .model_base import ModelBase

class Cards(ModelBase):
    __tablename__: str = 'cards'
    
    id: int = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    creat_date: datetime = sa.Column(sa.DateTime, default=datetime.now, index=True)
    data_modificacao: datetime = sa.Column(sa.DateTime, default=datetime.now, index=True)
    
    texto: str = sa.Column(sa.String(255), nullable=False)
    tag: str = sa.Column(sa.String(45), nullable=False)

    def __repr__(self) -> str:
        return f'<Cards>'