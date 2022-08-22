from card_app import app
from flask import render_template, request

import csv

@app.route("/export")
def export_file():
    
    title = ['text', 'tag']
    
    lista_cards = [{'text': 'Lorem ipsum dolor sit amet.', 'tag': 'tag1'}, 
                    {'text': 'Lorem ipsum dolor sit amet.', 'tag': 'tag2'}, 
                    {'text': 'Lorem ipsum dolor sit amet.', 'tag': 'tag3'}]
    
    with open('./file-export.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=title) 
        writer.writeheader() 
        writer.writerows(lista_cards)
    
    return "<p>Export file completed</p>"
