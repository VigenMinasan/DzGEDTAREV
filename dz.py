from flask import Flask, jsonify, request

app = Flask(__name__)

spisok = [
    {'id': 1, 'name': 'Артем', 'familia': 'Дегтярев'},
    {'id': 2, 'name': 'Антон', 'familia': 'Дегтярев'},
    {'id': 3, 'name': 'Артур', 'familia': 'Дегтярев'}
]

@app.route('/zap', methods=['GET', 'POST'])
def zap_func():
    if request.method == 'GET':
        return jsonify(spisok)
    elif request.method == 'POST':
        data = request.get_json() 
        spis = {
            'id': len(spisok) + 1,
            'name': data['name'],  # Доступ к ключам из JSON
            'familia': data['familia']
        }
        spisok.append(spis)
        return jsonify(spis), 201


@app.route('/zap', methods=['GET', 'POST'])
def zap_func():
    if request.method == 'GET':
        return jsonify(spisok)
    elif request.method == 'POST':
        data = request.get_json() 
        spis = {
            'id': len(spisok) + 1,
            'name': data['name'],  # Доступ к ключам из JSON
            'familia': data['familia']
        }
        spisok.append(spis)
        return jsonify(spis), 201

@app.route('/del/<int:spisok_id>', methods=['PUT', 'DELETE'])
def zapp_func(spisok_id):
    spisok_id -= 1
    if spisok_id < 0 or spisok_id >= len(spisok):
        return jsonify({'error': 'Плохие данные'}), 404
    del spisok[spisok_id]
    return jsonify({'message': 'Данные удалены'}), 204


@app.route('/zap', methods=['GET', 'POST'])
def zap_func():
    if request.method == 'GET':
        return jsonify(spisok)
    elif request.method == 'POST':
        data = request.get_json() 
        spis = {
            'id': len(spisok) + 1,
            'name': data['name'],  # Доступ к ключам из JSON
            'familia': data['familia']
        }
        spisok.append(spis)
        return jsonify(spis), 201

@app.route('/del/<int:spisok_id>', methods=['PUT', 'DELETE'])
def zapp_func(spisok_id):
    spisok_id -= 1
    if spisok_id < 0 or spisok_id >= len(spisok):
        return jsonify({'error': 'Плохие данные'}), 404
    del spisok[spisok_id]
    return jsonify({'message': 'Данные удалены'}), 204

@app.route('/update/<int:spisok_id>', methods=['PUT'])
def update_func(spisok_id):
    spisok_id -= 1
    if spisok_id < 0 or spisok_id >= len(spisok):
        return jsonify({'error': 'Плохие данные'}), 404

    data = request.get_json()
    spisok[spisok_id]['name'] = data.get('name', spisok[spisok_id]['name'])
    spisok[spisok_id]['familia'] = data.get('familia', spisok[spisok_id]['familia'])
    return jsonify(spisok[spisok_id]), 200




if __name__ == '__main__':
    app.run(debug=True)