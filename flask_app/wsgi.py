from app import app
import warnings
if __name__ == "__main__":
    warnings.filterwarnings('ignore')
    app.run(host='0.0.0.0', port=8000)

