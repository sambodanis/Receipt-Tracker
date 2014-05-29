from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['POST'])
def pull():
    return 'Hello World!a'

if __name__ == '__main__':
    app.run(host='0.0.0.0',
            port=9001)
