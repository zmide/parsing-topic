from flask import Flask
from blueprint import blueprintApp

app = Flask(__name__)
app.register_blueprint(blueprintApp)

if __name__ == '__main__':
    app.run(debug=True)
