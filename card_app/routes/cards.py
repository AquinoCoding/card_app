from card_app import app
from flask import render_template, request

# libs
import json
import time
from datetime import datetime

# services
from card_app.services.format_data import formata_data
from card_app.services.check_verify_bd import check_exist_tag

from card_app.services.insert_bd import insert_card
from card_app.services.read_bd import read_card, read_card_filter, read_card_single
from card_app.services.edit_bd import edit_card
from card_app.services.delete_bd import delete_card

# db
from card_app.database.db_session import create_session

# models
from card_app.models.card_model import Cards
from card_app.models.tag_model import Tags


# add Card
@app.route("/add-card", methods=["POST"])
def add_card():
    
    try:
        texto = request.json["texto"]
        tag = request.json["tag"]
        
    except Exception as e:
        return {"datetime": datetime.today(),
                "error": f"O parametro: {e} é obrigatorio"}
        
    if tag == '': tag = 'all'
    
    for i_tag in tag.split(";"):
        tags = check_exist_tag(i_tag)
        if not tags: return {"datetime": datetime.today(),
                            "error": f'{i_tag} não encontrada'}

    insert_card(texto, tag)
        
    return {"datetime": datetime.today(),
            "mensagem": "Adição concluida com sucesso"}

# all Cards
@app.route("/card", methods=["GET"])
def get_cards():
         
    content_cards = read_card()

    return {"datetime": datetime.today(),
            "data": str(content_cards)}

# filter tags all card
@app.route("/card/tag=<tag>", methods=["GET"])
def get_cards_filter_(tag):
    
    # check existing tag
    tags = check_exist_tag(tag)

    if not tags: return {"datetime": datetime.today(),
                        "error": 'tag não encontrada'}
            
    content_cards = read_card_filter(tag)

    return {"datetime": datetime.today(),
            "data": str(content_cards)}

# single Card
@app.route("/card/<id_>", methods=["GET"])
def get_card(id_):
    
    cards = read_card_single(id_)
    
    if not cards: return {"datetime": datetime.today(),
                        "mensagem": "Não encontrado"}

    return {"datetime": datetime.today(),
            "data": str({"id": cards.id, "texto": cards.texto, 
                         "tag": cards.tag, "creat_date": cards.creat_date, 
                         "data_modificacao": cards.data_modificacao})}

# Update Card
@app.route("/card/<id_>", methods=["PUT"])
def update_card(id_):
    
    try:
        texto = request.json["texto"]
        tag = request.json["tag"]
    
    except Exception as e: 
        error = f"O parametro: {e} é obrigatorio"
        return {"datetime": datetime.today(),
                "error": error}
        
    tags = check_exist_tag(tag)
        
    if not tags: return {"datetime": datetime.today(),
                        "error": 'tag não encontrada'}
    
    edit_card(id_, texto, tag)

    return {"datetime": datetime.today(),
            "mensagem": "Alteracao concluida com sucesso"}

# Delete Card
@app.route("/card/<id_>", methods=["DELETE"])
def del_card(id_):
    
    if delete_card(id_):
        return {"datetime": datetime.today(),
                "mensagem": "Delete concluido com sucesso"}
    
    else: return {"datetime": datetime.today(),
                      "mensagem": "Não encontrado"}
