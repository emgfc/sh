from app import app, db
import api.models
import api.views

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)