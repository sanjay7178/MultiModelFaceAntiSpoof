from app import server
import warnings
if __name__ == "__main__":
    warnings.filterwarnings('ignore')
    server.run(host='0.0.0.0', port=8000)

