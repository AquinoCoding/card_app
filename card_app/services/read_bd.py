# libs
from datetime import datetime

# models
from card_app.models.card_model import Cards
from card_app.models.tag_model import Tags

# db
from card_app.database.db_session import create_session

def read_card():
    with create_session() as session:
        cards: Cards = session.query(Cards)
        content_cards = [{"id": an.id, "texto": an.texto, 
                        "tag": an.tag, "data_criacao": an.creat_date} 
                            
                            for an in cards]
        
        return content_cards

def read_card_filter(tag: str):

    with create_session() as session:
        cards: Cards = session.query(Cards)
        
        content_cards = [{"id": an.id, "texto": an.texto, 
                        "tag": an.tag, "data_criacao": an.creat_date} 
                         
                         for an in cards if tag in an.tag.split(';')]

        return content_cards

def read_card_single(id_: str):
    with create_session() as session:
        cards: Cards = session.query(Cards).filter(Cards.id == id_).one_or_none()
    
    return cards

# Read Tags

def read_tag_single(id_: str):
    with create_session() as session:
        tags: Tags = session.query(Tags).filter(Tags.id == id_).one_or_none()
        
    if not tags: return {"datetime": datetime.today(),
                        "mensagem": "Não encontrado"}
    
    return tags

def read_tag():
    with create_session() as session:
        tags: Tags = session.query(Tags)
        content_tags = [{"id": an.id, "name": an.name, 
                        "data_criacao": an.creat_date}
                            
                            for an in tags]
        return content_tags

