from flask import Flask, request, redirect, render_template, url_for, session


app = Flask(__name__)
app.config['DEBUG'] = True
# set a secret key for the app so that the session object can be used
app.secret_key = b'\xaf\xec\\\xb6\xab\xbf\x9d\xc8an\x03\x04\x19q\x9d\nn\xf2\x91\x12,@\xa3\xed'

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    # remove the username from the session if it is there
    session.pop('username', None)

    if request.method == "GET":
        return render_template('signup.html',
            title = "Signup")

    elif request.method == "POST":
        username_error = ''
        username = request.form['username']

        password_error = ''
        password = request.form['password']

        verify_password_error = ''
        verify_password = request.form['verify_password']

        email_error = ''
        email = request.form['email']

        username_length = len(username)
        # check for empty username
        if username_length == 0:
            username_error = "Username is required"
        # check username length (should be between 3 and 20)
        elif username_length < 3 or username_length > 20:
            username_error = "Username must be between 3 and 20 characters long"
        
        password_length = len(password)
        # check for empty password
        if password_length == 0:
            password_error = "Password is required"
        # check password length (should be between 3 and 20)
        elif password_length < 3 or password_length > 20:
            password_error = "Password must be between 3 and 20 characters long"

        # check for empty verify_password
        if len(verify_password) == 0:
            verify_password_error = "Verify Password is required"
        # check for verify_password different than password
        elif verify_password != password:
            verify_password_error = "Passwords must match exactly"

        # Verify email if present (single '@', single '.',
        # no spaces and between 3 and 20 characters long)
        email_length = len(email)
        if email_length != 0:
            if email_length < 3 or email_length > 20:
                email_error = "Email must be between 3 and 20 characters"
            elif ' ' in email:
                email_error = "Email cannot contain spaces"
            elif email.count('@') != 1:
                email_error = "Email must contain exactly one '@'"
            elif email.count('.') != 1:
                email_error = "Email must contain exactly one '.'"

        if (not username_error and 
            not password_error and
            not verify_password_error and
            not email_error ):
            # no errors occured so redirect to the welcome page
            # store the username in the session object to avoid 
            # using query parameters
            session['username'] = username
            return redirect(url_for('welcome'))
        else:
            # an error occurred so redisplay the signup form with
            # error messages

            return render_template('signup.html',
                title = "Signup",
                username_error = username_error,
                password_error = password_error,
                verify_password_error = verify_password_error,
                email_error = email_error,
                # preserve username and email fields
                # clear the password fields
                username = username,
                email = email
            )
    else:
        return "Some how an invalid method of " + request.method + " slipped through!"


@app.route('/welcome')
def welcome():
    if 'username' not in session:
      return "You are not logged in!"

    username = session['username']
    return render_template('welcome.html', username=username)
    
app.run()
