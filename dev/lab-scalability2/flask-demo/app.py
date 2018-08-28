from flask import Flask
import os
import uuid

app = Flask(__name__)

@app.route('/')
def index():
    hostname = os.uname()[1]
    randomid = uuid.uuid4()
    return 'Container Hostname: ' + hostname + ' , ' + 'UUID: ' + str(randomid) + '\n'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)