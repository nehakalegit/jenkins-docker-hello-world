from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return jsonify(
        message='Welcome to the Jenkins Docker Hello World App!',
        endpoints={
            'home': '/',
            'greet': '/greet?name=YourName'
        }
    )

@app.route('/greet', methods=['GET'])
def greet():
    name = request.args.get('name', 'World')
    return jsonify(message=f'Hello World, {name}!')   

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)     