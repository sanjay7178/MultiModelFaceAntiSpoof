import os
from flask import Flask, render_template, request, flash, redirect, url_for, send_from_directory, jsonify
from m6 import predict_one_img
import warnings
import urllib.request
#from app import app
app = Flask(__name__)
from models.m7.model import M7FaceAntiSpoofing
from models.m6.model import M6FaceAntiSpoofing
import os
app.config['UPLOAD_FOLDER'] = 'static/uploads'

from flask import Flask, request, redirect, jsonify
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/file-upload', methods=['POST'])
def upload_file():
        # check if the post request has the file part
        if 'file' not in request.files:
                resp = jsonify({'message' : 'No file part in the request'})
                resp.status_code = 400
                return resp
        file = request.files['file']
        if file.filename == '':
                resp = jsonify({'message' : 'No file selected for uploading'})
                resp.status_code = 400
                return resp
        if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                resp = jsonify({'message' : 'File successfully uploaded'})
                resp.status_code = 201
                return resp
        else:
                resp = jsonify({'message' : 'Allowed file types are txt, pdf, png, jpg, jpeg, gif'})
                resp.status_code = 400
                return resp

@app.route('m7', methods=['POST'])
def m1():
        if 'file' not in request.files:
                resp = jsonify({'message' : 'No file part in the request'})
                resp.status_code = 400
                return resp
        file = request.files['file']
        if file.filename == '':
                resp = jsonify({'message' : 'No file selected for uploading'})
                resp.status_code = 400
                return resp
        if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                # call predict_one_img here
                x  = predict_one_img(os.path.join(app.config['UPLOAD_FOLDER'], filename),M7FaceAntiSpoofing())
                resp = jsonify({'message' : 'File successfully uploaded','result':x})

if __name__ == "__main__":
        warnings.filterwarnings('ignore')
        app.run(host='0.0.0.0')
