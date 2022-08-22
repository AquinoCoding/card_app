from card_app import app

import csv

from card_app.services.insert_bd import insert_card, insert_tag

@app.route("/import")
def import_file():
    
    with open('./file-import.csv', 'r') as csvfile:
        data_files = csv.DictReader(csvfile)

        for data in data_files:
            
            if data["tag"] == '': data["tag"] = 'all'
            insert_card(data["text"], data["tag"])
            
            for i_tag in data["tag"].split(";"):
                insert_tag(i_tag)
    
    return "<p>Import file completed</p>"

        