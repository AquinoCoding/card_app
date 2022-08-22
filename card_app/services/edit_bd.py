# libs
from datetime import datetime

# models
from card_app.models.card_model import Cards
from card_app.models.tag_model import Tags

# db
from card_app.database.db_session import create_session

def edit_card(id_: str, texto: str, tag: str):
    
    with create_session() as session:
        cards: Cards = session.query(Cards).filter(Cards.id == id_).one_or_none()
        
        if cards:
            cards.texto = texto
            cards.data_modificacao = datetime.now()
            cards.tag = tag

            session.commit()
        
        else:
            return {"datetime": datetime.today(),
                    "mensagem": "Não encontrado"}
            
def edit_tag(id_: str, name: str):
    
    with create_session() as session:
        tags: Tags = session.query(Tags).filter(Tags.id == id_).one_or_none()
        
        if tags:
            tags.name = name
            
            session.commit()
        
        else: 
            return {"datetime": datetime.today(),
                    "mensagem": "Não encontrado"}

