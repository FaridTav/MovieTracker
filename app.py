import mysql.connector
from mysql.connector import Error
from flask import Flask, request, render_template, jsonify

app = Flask(__name__, static_url_path='/static')


movies = []
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/movie', methods=['POST'])
def movie():
    data = request.get_json()
    new_movie = data['movie_content']
    movies.append(new_movie)
    return new_movie

@app.route('/movies', methods=['GET'])
def get_movies():
    return jsonify(movies)

@app.route('/movies/<int:movie_id>', methods=['DELETE'])
def delete_movie(movie_id):
    if movie_id < 0 or movie_id >= len(movies):
        return jsonify({"error": "Movie not found"}), 404
    movies.pop(movie_id)
    return '', 204

# ---Custom Error pages---
#invalid link
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

#internal server error
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)