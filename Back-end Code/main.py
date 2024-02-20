from my_app import create_app
from flask_cors import CORS

app = create_app()

if __name__ == '__main__':
    CORS(app)
    app.run(debug=True)