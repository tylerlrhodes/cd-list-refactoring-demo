""" Web App for Music CD Program """

import os
import csv
from math import ceil
from pathlib import Path
from flask import Flask
from flask import jsonify
from flask import request
from flask import Response
from flask_cors import CORS
from werkzeug.utils import secure_filename
from linked_list import LinkedList
from list_store import ThreadSafeListStore
from music_cd import MusicCD

app = Flask(__name__)
#cors = CORS(app, resources={r"*": {"origins": "*"}})
CORS(app)

UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = {'csv'}

CDS_PER_PAGE = 10

app.config['UPLOAD_FOLDER'] = Path(UPLOAD_FOLDER)

store = ThreadSafeListStore(LinkedList(None))
store.append(MusicCD("Radiohead", "Kid A", 2006, 0))
store.append(MusicCD("Radiohead", "The Bends", 2006, 1))
store.append(MusicCD("Dave Matthews Band", "Under the Table and Dreaming", 2002, 2))

def sort_helper(item, column):
    """ Help pick the sort key """
    column = column.lower()
    if column == 'artist':
        return item.artist
    if column == 'title':
        return item.title
    return item.year

@app.route('/GetCDS')
@app.route('/GetCDS/<int:page>')
@app.route('/GetCDS/<int:page>/<string:sort_column>/<int:sort_direction>')
def get_cds(page = None, sort_column = 'artist', sort_direction = 1):
    """ API Endpoint for getting CD List """
    if page is None:
        page = 0
    reverse = False
    if sort_direction == 2:
        reverse = True
    total_pages = ceil(len(store) / CDS_PER_PAGE)
    start = page * CDS_PER_PAGE
    end = page * CDS_PER_PAGE + CDS_PER_PAGE

    sorted_store = sorted(store,
                          key=lambda x: sort_helper(x, sort_column), 
                          reverse=reverse)
    sorted_page = sorted_store[start:end]
    cd_list = []
    for cd in sorted_page:
        cd_list.append([cd.artist, cd.title, cd.year, cd.cdid])

    returnVal = {'total_pages':total_pages, 
                 'cd_list':cd_list,
                 'per_page':CDS_PER_PAGE,
                 'sort_column': sort_column,
                 'sort_direction': sort_direction}

    return jsonify(returnVal)

@app.route('/DownloadCSV')
def download_csv():
    """ Download the CDs in CSV format """
    def gen():
        yield 'artist, title, year' + '\n'
        cd_list = []
        for cd in store:
            cd_list.append([f'"{cd.title}"', f'"{cd.artist}"', f'"{str(cd.year)}"'])
        for row in cd_list:
            yield ','.join(row) + '\n'
    return Response(gen(), mimetype='text/csv', headers={
        "Content-disposition":"attachment; filename=cds.csv"})

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

    store.append(MusicCD(artist, title, year, 0))

    return f"{json}"


def update_cd_list_from_csv(current_csv_file):
    """ Take csv file and put it to CD Store """
    global store
    with open(current_csv_file, newline='') as f:
        new_list = ThreadSafeListStore(LinkedList(None))
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            print(row)
            new_list.append(MusicCD(row[0], row[1], row[2], 0))
        store = new_list

def allowed_file(filename):
    """ Allowed filename helper """
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/UploadCSV', methods=['POST'])
def upload_file():
    """ Upload CSV list of CDs """
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
            update_cd_list_from_csv(current_csv_file)
            return jsonify({'Result': True})
