from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
import random
from seed import seed_db
from models import db, Joke
from flask import abort

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///jokes.db')

db.init_app(app)
@app.before_request
def before_request():
    api_key = request.headers.get('x-api-key')
    if not api_key or api_key != os.environ.get('API_KEY'):
        abort(401, description="API key is missing or invalid.")

@app.route('/joke', methods=['GET'])
def get_joke():
    level = request.args.get('level')
    lang = request.headers.get('Accept-Language')

    # Construindo a consulta dinamicamente
    query = Joke.query
    if level:
        query = query.filter_by(level=level)
    if lang:
        query = query.filter_by(lang=lang)

    jokes = query.all()

    if not jokes:
        return jsonify({"message": "No jokes found matching the criteria."}), 404

    return jsonify([{"id": joke.id, "text": joke.text, "level": joke.level, "lang": joke.lang} for joke in jokes])

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        seed_db()
    app.run(debug=True, host='0.0.0.0', port=8001)
    print('Running app.py...')