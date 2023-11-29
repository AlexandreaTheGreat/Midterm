from flask import Flask, jsonify, request

app = Flask(__name__)

data = [
    {
        "heart_id": 1,
        "date": "November 29, 2023",
        "heart_rate": "28 bpm"
    }
]

@app.route('/heart', methods=['GET'])
def get_all_data():
    return jsonify(data)

@app.route('/heart', methods=['POST'])
def add_data():
    record = request.get_json()
    data.append(record)
    return jsonify(data)

@app.route('/heart/<heart_id>', methods=['GET'])
def get_data(heart_id):
    i = int(heart_id) - 1
    return jsonify(data[i])

@app.route('/heart/<heart_id>', methods=['PUT'])
def update_data(heart_id):
    i = int(heart_id) - 1
    record = request.get_json()
    data[i].update(record)
    return jsonify(data[i])

@app.route('/heart/<heart_id>', methods=['DELETE'])
def delete_data(heart_id):
    i = int(heart_id) - 1
    data.pop(i)
    return jsonify(data)

if __name__ == '__main__':
    app.run()