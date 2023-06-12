
<h3 align="center">MultiModelFaceAntiSpoof</h3>

<p align="center">
  🚀 MultiModelFaceAntispoof utilizes Multiple Open Source Spoofing models for Inference via Flask API. It integrates multiple face anti-spoofing models from GitHub. Contributions, corrections, and requests are welcomed on GitHub.
</p>
<p align="center">
  <a href="https://github.com/sanjay7178/actions/checkout/actions/runs/">
    <img src="https://img.shields.io/github/sanjay7178/workflow/status/actions/checkout/CI?logo=github&label=tests" alt="Build status">
  </a>
  
  <a href="https://pypi.org/project/[flasgger/">
    <img src="https://img.shields.io/pypi/v/flasgger?logo=python&logoColor=white" alt="PyPI version">
  </a>

  <img src="https://img.shields.io/badge/Docker%20Passing-2496ED?logo=docker&logoColor=white" alt="Docker Passing">

  <img src="https://img.shields.io/badge/GitHub%20Actions-2088FF?logo=github%20actions&logoColor=white" alt="GitHub Actions">

  <img src="https://img.shields.io/badge/Docker%20Compose-2496ED?logo=docker&logoColor=white" alt="Docker Compose">

  <img src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white" alt="Python">

  <img src="https://img.shields.io/badge/TensorFlow-FF6F00?logo=tensorflow&logoColor=white" alt="TensorFlow">

  <img src="https://img.shields.io/badge/PyTorch-EE4C2C?logo=pytorch&logoColor=white" alt="PyTorch">

  <img src="https://img.shields.io/badge/MTCNN-N%2FA" alt="MTCNN">

  <img src="https://img.shields.io/badge/Flask-000000?logo=flask&logoColor=white" alt="Flask">

  <img src="https://img.shields.io/badge/Gunicorn-37404F?logo=gunicorn&logoColor=white" alt="Gunicorn">

  <img src="https://img.shields.io/badge/Nginx-009639?logo=nginx&logoColor=white" alt="Nginx">
</p>

MultiModelFaceAntiSpoof is [available on Docker Hub](https://hub.docker.com/r/sanjay7178/facespoof).



### Installation
Setup
```
sudo apt install  git-lfs -y
git  clone https://github.com/sanjay7178/MultiModelFaceAntiSpoof
cd MultiModelFaceAntiSpoof
git-lfs pull
```
Inference
```
docker-compose  up  --build -d
```

### Try Out on Google Colab
<div>
  <a href="https://colab.research.google.com/drive/1M3GIDJVXQk0LYTxvXoOK8t6v3CxZUk-6?usp=sharing">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" target="_blank" alt="Open In Colab">
  </a>
</div>

<br>

🔬 Spoof Detection Models:

1. [M1: HyperFAS](https://github.com/zeusees/HyperFAS)
2. [M2: Face Anti-Spoofing](https://github.com/emadeldeen24/face-anti-spoofing)
3. [M3: CelebA-Spoof](https://github.com/Davidzhangyuanhan/CelebA-Spoof)
4. [M4: Awesome Face Antispoofing](https://github.com/JinghuiZhou/awesome_face_antispoofing)
5. M5: Simple CNN model (trained from scratch)
6. [M6: Silent-Face-Anti-Spoofing](https://github.com/minivision-ai/Silent-Face-Anti-Spoofing)
7. [M7: Face-Anti-Spoofing-using-DeePixBiS](https://github.com/Saiyam26/Face-Anti-Spoofing-using-DeePixBiS)
8. [M8: FaceAntiSpoofing](https://github.com/pourfard/FaceAntiSpoofing)

### Requirements:
- Python 3.6 or higher
- Upgrade pip: `pip3 install pip --upgrade`
- Install required packages: `pip3 install -r requirements.txt`

### Usage:
- Run the test script: `python3 test.py`

### TODO:
1. Add more spoof detection models

## Credits and Source
Original repository: [FaceAntiSpoofing](https://github.com/pourfard/FaceAntiSpoofing)
