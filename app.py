import mysql.connector
from mysql.connector import Error
from flask import Flask, request, render_template, jsonify

app = Flask(__name__, static_url_path='/static')
cnx = mysql.connector.connect(user='root',
                                  password='Soccer12345!',
                                  host='localhost',
                                  database='Movie')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/movie', methods=['POST'])
def movie():
    data = request.get_json()
    if not data or 'movieName' not in data:
        return jsonify({"error": "movieName is required"}), 400 #this is to see what the heck the problem is
    
    new_movie = data['movieName']
    cursor = cnx.cursor()
    cursor.execute("INSERT INTO movies (movieName) VALUES (%s)", (new_movie,))
    cnx.commit()
    cursor.close()
    return jsonify({"message": "Movie added successfully"}), 201

@app.route('/movies', methods=['GET'])
def get_movies():
    cursor = cnx.cursor()
    cursor.execute("SELECT * FROM movies")
    movies = cursor.fetchall()
    cursor.close()
    return jsonify(movies)

@app.route('/movies/<int:movie_id>', methods=['DELETE'])
def delete_movie(movie_id):
    cursor = cnx.cursor()
    cursor.execute("DELETE FROM movies WHERE id = %s", (movie_id,))
    cnx.commit()
    cursor.close()
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