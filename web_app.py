""" Web App for Music CD Program """
from flask import Flask
from flask import jsonify
from flask_cors import CORS
from linked_list import LinkedList
from music_cd import MusicCD

app = Flask(__name__)
CORS(app)

@app.route('/GetCDS')
def get_cds():
    """ API Endpoint for getting CD List """
    cds = LinkedList(None)
    cds.add_to_list(MusicCD("Kid A", "Radiohead", 2006, 0))
    cds.add_to_list(MusicCD("The Bends", "Radiohead", 2006, 1))
    cds.add_to_list(MusicCD("Dave Matthews Band", "Under the Table and Dreaming", 2002, 2))
    cd_list = []
    for cd in cds:
        cd_list.append([cd.item.title, cd.item.artist, cd.item.year, cd.item.cdid])
    return jsonify(cd_list)
