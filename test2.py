from models.m7.model import M7FaceAntiSpoofing
import os
# from m6 import predict_one_img
import warnings
from detector.cv_face_detector.model import CVFaceDetector
face_detector = CVFaceDetector()
spoof_detectors = [M7FaceAntiSpoofing()]
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
            return False
        else:
            return True
x  = predict_one_img("benchmarks/fake/fake1.jpg", spoof_detectors[0])
print(x)
