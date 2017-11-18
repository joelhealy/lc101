from flask import Flask, request, redirect, render_template, url_for, session


app = Flask(__name__)
app.config['DEBUG'] = True
# set a secret key for the app so that the session object can be used
app.secret_key = b'\xaf\xec\\\xb6\xab\xbf\x9d\xc8an\x03\x04\x19q\x9d\nn\xf2\x91\x12,@\xa3\xed'

@app.route('/signup', methods=['GET', 'POST'])
def index():
    # remove the username from the session if it is there
    session.pop('username', None)
    if request.method == "GET":
        return render_template('signup.html',
            title="Signup"
        )
    elif request.method == "POST":
        username = request.form['username']
        if len(username) == 0:
            username_error = "Username is required"
            return render_template('signup.html',
                title =" Signup",
                username_error = username_error
            )
        # store the username in the session object to avoid query parameters
        session['username'] = username
        return redirect(url_for('welcome'))
    else:
        return 'This code should have been unreachable: ID=dkcok134'

@app.route('/welcome')
def welcome():
    if 'username' not in session:
      return "You are not logged in!"

    username = session['username']
    return render_template('welcome.html', username=username)
    
app.run()
