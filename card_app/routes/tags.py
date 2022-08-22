from card_app import app
from flask import render_template, request

# libs
import json
from datetime import datetime

# db
from card_app.database.db_session import create_session

# services
from card_app.services.format_data import formata_data

from card_app.services.insert_bd import insert_card, insert_tag
from card_app.services.read_bd import read_card, read_card_filter, read_card_single, read_tag, read_tag_single
from card_app.services.edit_bd import edit_card, edit_tag
from card_app.services.delete_bd import delete_card, delete_tag


# add Tag
@app.route("/add-tag", methods=["POST"])
def add_tag():
    
    try:
        name = request.json["name"]
        
    except Exception as e: 
        error = f"O parametro: {e} é obrigatorio"
        return {"datetime": datetime.today(),
                "error": error}
    
    for i_tag in name.split(";"):
        insert_tag(i_tag)
        
    return {"datetime": datetime.today(),
            "mensagem": "Adição concluida com sucesso"}

# all Tags
@app.route("/tags", methods=["GET"])
def get_tags():
    
    content_tags = read_tag()

    return {"datetime": datetime.today(),
            "data": str(content_tags)}

# single Tag
@app.route("/tag/<id_>", methods=["GET"])
def get_tag(id_):
    
    tags = read_tag_single(id_)
        
    return {"datetime": datetime.today(),
            "data": str({"id": tags.id, "name": tags.name, "data_criacao": tags.creat_date})}

# Update Tag
@app.route("/tag/<id_>", methods=["PUT"])
def update_tag(id_):
    
    try:
        name = request.json["name"]
    
    except Exception as e: 
        return {"datetime": datetime.today(),
                "error": f"O parametro: {e} é obrigatorio"}
        
    edit_tag(id_, name)

    return {"datetime": datetime.today(),
            "mensagem": "Alteracao concluida com sucesso"}

# Delete Card
@app.route("/tag/<id_>", methods=["DELETE"])
def del_tag(id_):
    
    if delete_tag(id_):
        return {"datetime": datetime.today(),
                "mensagem": "Delete concluido com sucesso"}
    
    else: return {"datetime": datetime.today(),
                      "mensagem": "Não encontrado"}
