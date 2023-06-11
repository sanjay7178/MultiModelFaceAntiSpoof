import os
from flask import Flask, render_template, request, flash, redirect, url_for, send_from_directory, jsonify

#from models.m2.model import M2FaceAntiSpoofing
from models.m7.model import M7FaceAntiSpoofing
from models.m6.model import M6FaceAntiSpoofing
import os
from models.m1.model import M1FaceAntiSpoofing
# from m6 import predict_one_img
import warnings
from detector.cv_face_detector.model import CVFaceDetector
face_detector = CVFaceDetector()
spoof_detectors = [M7FaceAntiSpoofing(),M6FaceAntiSpoofing(),M1FaceAntiSpoofing()]
import urllib.request
import cv2

def predict_one_img(img_path,  spoof_detector):
    bgr = cv2.imread(img_path)
    face_bboxes = face_detector.get_face_bboxes(bgr)
    for bbox in face_bboxes:
        crop = bgr[bbox[1]:bbox[3], bbox[0]:bbox[2], :]
        real_score = spoof_detector.get_real_score(bgr, bbox)
        print("Real score for image name " + img_path + " is: ",
              real_score)
        if real_score < 0.5:
            return False, real_score
        else:
            return True ,real_score

import warnings
import urllib.request
#from app import app
app = Flask(__name__)
from models.m7.model import M7FaceAntiSpoofing
from models.m6.model import M6FaceAntiSpoofing
import os
from flasgger import Swagger
swagger = Swagger(app, template={
 "swagger": "2.0",
 "info": {
  "title": "Inference",
  "version": "1.0.0"
 }
})

app.config['UPLOAD_FOLDER'] = 'static/uploads'

from flask import Flask, request, redirect, jsonify
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/m7', methods=['POST'])
def m7_upload_file():
        """
        Upload Image and get mask, bounded box coordinates and label     
        ---
        parameters:
          - in: formData
            name: file
            type: file
            required: true
        responses:
          200:
            description: gets output
          400:
            description: input not supported
        """
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
                print(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                x, y  = predict_one_img(os.path.join(app.config['UPLOAD_FOLDER'], filename), spoof_detectors[0])
                print(x)
                resp = jsonify({'message' : 'File successfully uploaded', 'result': x, 'real_score':y}  )
                resp.status_code = 201
                return resp
        else:
                resp = jsonify({'message' : 'Allowed file types are txt, pdf, png, jpg, jpeg, gif'})
                resp.status_code = 400
                return resp

@app.route('/m6', methods=['POST'])
def m6_upload_file():
        """
        Upload Image and get mask, bounded box coordinates and label     
        ---
        parameters:
          - in: formData
            name: file
            type: file
            required: true
        responses:
          200:
            description: gets output
          400:
            description: input not supported
        """
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
                print(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                x ,y  = predict_one_img(os.path.join(app.config['UPLOAD_FOLDER'], filename), spoof_detectors[1])
                print(x)
                resp = jsonify({'message' : 'File successfully uploaded', 'result': x, 'real_score':y}  )
                resp.status_code = 201
                return resp
        else:
                resp = jsonify({'message' : 'Allowed file types are txt, pdf, png, jpg, jpeg, gif'})
                resp.status_code = 400
                return resp
'''
@app.route('/m2', methods=['POST'])
def m2_upload_file():
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
                print(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                x ,y  = predict_one_img(os.path.join(app.config['UPLOAD_FOLDER'], filename), spoof_detectors[2])
                print(x)
                resp = jsonify({'message' : 'File successfully uploaded', 'result': x, 'real_score':y}  )
                resp.status_code = 201
                return resp
        else:
                resp = jsonify({'message' : 'Allowed file types are txt, pdf, png, jpg, jpeg, gif'})
                resp.status_code = 400
                return resp

'''
@app.route('/m1', methods=['POST'])
def m1_upload_file():
        """
        Upload Image and get mask, bounded box coordinates and label     
        ---
        parameters:
          - in: formData
            name: file
            type: file
            required: true
        responses:
          200:
            description: gets output
          400:
            description: input not supported
        """
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
                print(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                x ,y  = predict_one_img(os.path.join(app.config['UPLOAD_FOLDER'], filename), spoof_detectors[2])
                print(x)
                resp = jsonify({'message' : 'File successfully uploaded', 'result': x, 'real_score':y}  )
                resp.status_code = 201
                return resp
        else:
                resp = jsonify({'message' : 'Allowed file types are txt, pdf, png, jpg, jpeg, gif'})
                resp.status_code = 400
                return resp

# if __name__ == "__main__":
#         warnings.filterwarnings('ignore')
#         app.run(host='0.0.0.0')
