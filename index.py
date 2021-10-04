#!/usr/bin/env python

import flask
import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
from flask import send_from_directory

UPLOAD_FOLDER = 'images'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def index():
    """ Displays the index page accessible at '/'
    """
    return flask.render_template('index.html')
    
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],filename)

@app.route('/classification/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(path)
            print('---------------')
            print( 'filename = ',filename)
            
            text = get_response(path)
            
            return flask.render_template('response.html',resp_text=text)
            #return "<!doctype html><title>Your response</title><h1>{}</h1>".format(text)
            #return redirect(url_for('uploaded_file',filename=filename))
    return flask.render_template('uploader.html')
    
    
    
def get_response(path):
    text = None
    #l'image est accessible avec le chemin path
    print('path = ',path)
    
    #chargez l'image avec la librairie que vous utilisez
    #image = 
    
    '''
    votre code ici
    
    text = 
    '''
    
    
    #retournez l'information sous forme d'un str 
    text = text if text else 'class found: covid detected' 
    
    return text 

if __name__ == '__main__':
    app.debug=True
    app.run()
    