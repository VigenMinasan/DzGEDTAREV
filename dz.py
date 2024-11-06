from flask import Flask, jsonify, request

app = Flask(__name__)

spisok = [
    {'id': 1, 'name': 'Артем', 'familia': 'Дегтярев'},
    {'id': 2, 'name': 'Антон', 'familia': 'Дегтярев'},
    {'id': 3, 'name': 'Артур', 'familia': 'Дегтярев'}
]
