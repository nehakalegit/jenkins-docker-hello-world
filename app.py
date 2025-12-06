# 1️⃣ Import Flask tools
from flask import Flask, request, jsonify

# 2️⃣ Start the web app
app = Flask(__name__)

# 3️⃣ Home page
# When someone visits "/", they see a welcome message
@app.route('/', methods=['GET'])
def home():
    return jsonify(
        message='Welcome to my simple Hello World App!',  # Welcome text
        endpoints={  # Shows other pages they can visit
            'home': '/',
            'greet': '/greet?name=YourName'
        }
    )

# 4️⃣ Greet page
# When someone visits "/greet", it says hello
# They can add their name in the URL like "/greet?name=Neha"
@app.route('/greet', methods=['GET'])
def greet():
    # Get the name from the URL. If no name is given, use "World"
    name = request.args.get('name', 'World')
    
    # Return a greeting message
    return jsonify(message=f'Hello World, {name}!')

# 5️⃣ Run the web app
# Opens the website on your computer at port 5000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
