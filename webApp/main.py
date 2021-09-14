from flask import Flask
from services import patient_service

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello Flask!'


if __name__ == '__main__':
    patient_service.hello_service()
    app.run()
