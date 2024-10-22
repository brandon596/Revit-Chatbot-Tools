from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Home"

@app.route('/calculate', methods=['POST'])
def calculate():
    # Get the expression from the client
    data = request.json
    expression = data.get('expression')
    
    try:
        # Evaluate the expression (e.g., "1+1")
        result = str(eval(expression))
    except Exception as e:
        return jsonify({'error': str(e)}), 400

    # Return the result
    return jsonify({'result': result})

@app.route('/get-video-urls', methods=["POST"])
def get_citations():
    citations = request.json
    print(citations)
    return jsonify({"result": "hello"}), 201

@app.route('/test-get/<user>')
def test(user):
    user_data = {
        "user": user,
        "name": "s",
        "email": "wrrwf"
    }
    return jsonify(user_data), 200

if __name__ == '__main__':
    app.run(debug=True)