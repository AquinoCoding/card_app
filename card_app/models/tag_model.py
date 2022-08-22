import sqlalchemy as sa

from datetime import datetime

from .model_base import ModelBase

class Tags(ModelBase):
    __tablename__: str = 'tags'
    
    id: int = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    creat_date: datetime = sa.Column(sa.DateTime, default=datetime.now, index=True)
    
    name: str = sa.Column(sa.String(45), nullable=False)

    def __repr__(self) -> str:
        return f'<Tags>'
