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

