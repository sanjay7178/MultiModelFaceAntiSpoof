from detector.FaceDetector import FaceDetectorInterface
from mtcnn import MTCNN
import cv2

class MTCNNFaceDetector(FaceDetectorInterface):
    def __init__(self):
        self.detector = MTCNN()

    def get_face_bboxes(self, bgr):
        detections = self.detector.detect_faces(bgr)
        result = []
        for detection in detections:
            x, y, width, height = detection['box']
            result.append([x, y, x + width, y + height])
        return result

