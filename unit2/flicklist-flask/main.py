from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True      # displays runtime errors in the browser, too

#app.config['SQLALCHEMY_DATABASE_URI'] = 'oracle://easoh:easoh@204.47.240.19:1521/r7lims'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://flicklist:MyNewPass@localhost:8889/flicklist'
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    watched = db.Column(db.Boolean)
    rating = db.Column(db.String(25))

    def __init__(self, name):
        self.name = name
        self.watched = False

    def __repr__(self):
        return '<Movie %r>' % self.name

# a list of movies that nobody should have to watch
terrible_movies = [
    "Gigli",
    "Star Wars Episode 1: Attack of the Clones",
    "Paul Blart: Mall Cop 2",
    "Nine Lives",
    "Starship Troopers"
]

def get_current_watchlist():
    # returns user's current watchlist -- a list of movies they want to see but haven't yet
    return Movie.query.filter_by(watched=False).all()

def get_watched_movies():
    # For now, we are just pretending
    # returns the list of movies the user has already watched and crossed off
    return Movie.query.filter_by(watched=True).all()


# Create a new route called rate_movie which handles a POST request on /rating-confirmation
@app.route("/rating-confirmation", methods=['POST'])
def rate_movie():
    movie_id = request.form['movie-id']
    rating = request.form['rating']
    movie = Movie.query.get(movie_id)

    if movie not in get_watched_movies():
        # the user tried to rate a movie that isn't in their list,
        # so we redirect back to the front page and tell them what went wrong
        error = "No movie with id:{0} is not in your Watched Movies list, so you can't rate it!".format(movie_id)

        # redirect to homepage, and include error as a query parameter in the URL
        return redirect("/?error=" + error)

    # if we didn't redirect by now, then all is well
    movie.rating = rating
    db.session.add(movie)
    db.session.commit()

    return render_template('rating-confirmation.html', movie=movie.name, rating=movie.rating)


# Creates a new route called movie_ratings which handles a GET on /ratings
@app.route("/ratings", methods=['GET'])
def movie_ratings():
    return render_template('ratings.html', movies = get_watched_movies())


@app.route("/crossoff", methods=['POST'])
def crossoff_movie():
    crossed_off_movie_id = int(request.form['crossed-off-movie-id'])
    crossed_off_movie = Movie.query.get(crossed_off_movie_id)

    if crossed_off_movie not in get_current_watchlist():
        # the user tried to cross off a movie that isn't in their list,
        # so we redirect back to the front page and tell them what went wrong
        error = "No movie with id:{0} is in your Watchlist, so you can't cross it off!".format(crossed_off_movie_id)

        # redirect to homepage, and include error as a query parameter in the URL
        return redirect("/?error=" + error)

    # if we didn't redirect by now, then all is well
    crossed_off_movie.watched = True
    db.session.add(crossed_off_movie)
    db.session.commit()
    return render_template('crossoff.html', crossed_off_movie_name=crossed_off_movie.name)


@app.route("/add", methods=['POST'])
def add_movie():
    # look inside the request to figure out what the user typed
    new_movie_name = request.form['new-movie']

    # if the user typed nothing at all, redirect and tell them the error
    if (not new_movie_name) or (new_movie_name.strip() == ""):
        error = "Please specify the movie you want to add."
        return redirect("/?error=" + error)

    # if the user wants to add a terrible movie, redirect and tell them the error
    if new_movie_name in terrible_movies:
        error = "Trust me, you don't want to add '{0}' to your Watchlist".format(new_movie_name)
        return redirect("/?error=" + error)

    # 'escape' the user's input so that if they typed HTML, it doesn't mess up our site
    new_movie_name_escaped = cgi.escape(new_movie_name, quote=True)

    new_movie = Movie(new_movie_name_escaped)
    db.session.add(new_movie)
    db.session.commit()

    return render_template('add-confirmation.html', movie=new_movie.name)


@app.route("/")
def index():
    encoded_error = request.args.get("error")
    return render_template('edit.html', watchlist=get_current_watchlist(), error=encoded_error and cgi.escape(encoded_error, quote=True))

if __name__ == "__main__":
    app.run()
