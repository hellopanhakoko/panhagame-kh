from flask import Flask, render_template, jsonify, request
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/game/snake')
def snake():
    return render_template('snake.html')

@app.route('/game/memory')
def memory():
    return render_template('memory.html')

@app.route('/game/tetris')
def tetris():
    return render_template('tetris.html')

@app.route('/game/math')
def math_game():
    return render_template('math.html')

@app.route('/game/math1')
def math_game1():
    return render_template('math1.html')
    
@app.route('/mine')
def index():
    return render_template('index1.html')

@app.route('/api/world')
def get_world():
    return jsonify({"status": "ok", "message": "Angkor Wat World"})

@app.route('/api/leaderboard', methods=['GET', 'POST'])
def leaderboard():
    # In-memory leaderboard (resets on restart)
    if not hasattr(app, 'scores'):
        app.scores = {}
    
    if request.method == 'POST':
        data = request.json
        game = data.get('game')
        name = data.get('name', 'Anonymous')
        score = data.get('score', 0)
        if game not in app.scores:
            app.scores[game] = []
        app.scores[game].append({'name': name, 'score': score})
        app.scores[game] = sorted(app.scores[game], key=lambda x: x['score'], reverse=True)[:10]
        return jsonify({'status': 'ok'})
    
    game = request.args.get('game', 'snake')
    return jsonify(app.scores.get(game, []))

if __name__ == '__main__':
    app.run(debug=True, port=5000)
