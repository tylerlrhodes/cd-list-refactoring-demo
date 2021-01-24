""" Web App for Music CD Program """

import os
import csv
from pathlib import Path
from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
from werkzeug.utils import secure_filename
from linked_list import LinkedList
from music_cd import MusicCD



app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})

UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = {'csv'}

app.config['UPLOAD_FOLDER'] = Path(UPLOAD_FOLDER)

cds = LinkedList(None)
cds.add_to_list(MusicCD("Radiohead", "Kid A", 2006, 0))
cds.add_to_list(MusicCD("Radiohead", "The Bends", 2006, 1))
cds.add_to_list(MusicCD("Dave Matthews Band", "Under the Table and Dreaming", 2002, 2))

current_csv_file = None

@app.route('/GetCDS')
def get_cds():
    """ API Endpoint for getting CD List """
    cd_list = []
    for cd in cds:
        cd_list.append([cd.item.title, cd.item.artist, cd.item.year, cd.item.cdid])
    return jsonify(cd_list)

@app.route('/AddCD', methods = ['POST'])
def add_cd():
    """ API Endpoint for adding a CD """
    try:
        json = request.get_json()
        artist = json["artist"]
        title = json["title"]
        year = json["year"]
    except KeyError as e:
        msg = str(e)
        return '{"error":"' + msg + '"}'

    cds.add_to_list(MusicCD(artist, title, year, 0))

    return f"{json}"


def update_cd_list_from_csv():
    global cds
    with open(current_csv_file, newline='') as f:
        new_list = LinkedList(None)
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            print(row)
            new_list.add_to_list(MusicCD(row[0], row[1], row[2], 0))
        cds = new_list

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/UploadCSV', methods=['POST'])
def upload_file():
    global current_csv_file
    if request.method == 'POST':
        # check if the post request has the file part
        if 'csvfile' not in request.files:
            raise KeyError
        file = request.files['csvfile']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            raise ValueError
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            current_csv_file = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(current_csv_file)
            update_cd_list_from_csv()
            return jsonify({'Result': True})