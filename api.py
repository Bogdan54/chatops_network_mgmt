from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/status', methods=['GET'])
def status():
    return jsonify({"router1": "Online", "switch1": "Offline"})

if __name__ == '__main__':
    app.run(port=5000, debug=True)
