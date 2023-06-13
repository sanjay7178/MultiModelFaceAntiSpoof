from models.FaceAntiSpoofing import FaceAntiSpoofingInterface 
import cv2 
import numpy as np 
import mediapipe as mp 
from models.m4.m4models import MyresNet34 
import tensorflow as tf

class M4FaceAntiSpoofing(FaceAntiSpoofingInterface):
  def __init__(self): 
    self.mp_drawing = mp.solutions.drawing_utils 
    self.mp_face_mesh = mp.solutions.face_mesh 
    MODEL_PATH = "models/m4/files/5.pth" 
    self.model = MyresNet34().eval() 
    self.model.load(MODEL_PATH) 
    self.model.train(False) 
    self.scale = 3.5 
    self.image_size = 224
  def process_image(self, image):
    with self.mp_face_mesh.FaceMesh(
        static_image_mode=True, max_num_faces=1, min_detection_confidence=0.5) as face_mesh:
        # Convert the BGR image to RGB.
        results = face_mesh.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

        if results.multi_face_landmarks:
            face_landmarks = []
            for face_landmark in results.multi_face_landmarks:
                coords = []
                for idx, landmark in enumerate(face_landmark.landmark):
                    coords.append([landmark.x, landmark.y])
                face_landmarks.append(np.array(coords))
            return face_landmarks[0]
        else:
            return None


  def crop_with_ldmk(self, image, landmark):
      ct_x, std_x = landmark[:, 0].mean(), landmark[:, 0].std()
      ct_y, std_y = landmark[:, 1].mean(), landmark[:, 1].std()
  
      std_x, std_y = self.scale * std_x, self.scale * std_y
  
      src = np.float32([(ct_x, ct_y), (ct_x + std_x, ct_y + std_y), (ct_x + std_x, ct_y)])
      dst = np.float32([((self.image_size - 1) / 2.0, (self.image_size - 1) / 2.0),
                        ((self.image_size - 1), (self.image_size - 1)),
                        ((self.image_size - 1), (self.image_size - 1) / 2.0)])
      retval = cv2.getAffineTransform(src, dst)
      result = cv2.warpAffine(image, retval, (self.image_size, self.image_size), flags=cv2.INTER_LINEAR,
                              borderMode=cv2.BORDER_CONSTANT)
      return result
  
  def get_real_score(self, bgr, face_bbox):
      rgb = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)
      face_landmark = self.process_image(bgr)
      if face_landmark is None:
          return 0.0
  
      ldmk = np.asarray(face_landmark, dtype=np.float32)
      ldmk = ldmk[np.argsort(np.std(ldmk[:, :, 1], axis=1))[-1]]
      result = self.crop_with_ldmk(bgr, ldmk)
      data = np.transpose(np.array(result, dtype=np.float32), (2, 0, 1))
  
      data = data[np.newaxis, :]
      data = tf.constant(data)
      with tf.device('/CPU:0'):
          outputs = self.model(data)
          outputs = tf.nn.softmax(outputs, axis=-1)
          preds = outputs.numpy()
          attack_prob = preds[:, 0]  # 0 attack 1 genuine
  
      return 1 - float(attack_prob[0])
  
