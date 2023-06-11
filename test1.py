from models.m7.model import M7FaceAntiSpoofing
import os
from m6 import predict_one_img
import warnings
import urllib.request


x = predict_one_img("benchmarks/fake/fake2.jpg",M7FaceAntiSpoofing())
print(x)
