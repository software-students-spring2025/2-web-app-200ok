import flask
import src.db as db
import config

app = flask.Flask(__name__)

db.init_db(app)

# Login get
@app.route('/login')
def login():
    return flask.render_template('login.html')

# Login post if user give username and password
@app.route('/login', methods=['POST'])
def handle_login():
    username = flask.request.form.get('username')
    password = flask.request.form.get('password')
    
    user = db.login_user(username, password)
    # Redirect if find match user in the database
    if user:  
        return flask.redirect('/home')

    return flask.render_template('login.html', message="Invalid username or password")

# Register get
@app.route('/register')
def register():
    return flask.render_template('register.html')

# Register the username and possword
@app.route('/register', methods=['POST'])
def handle_register():
    username = flask.request.form.get('username')
    password = flask.request.form.get('password')

    user = db.create_user(username, password)

    if user:  
        return flask.redirect('/home')

    return flask.render_template('register.html', message="Username Already Exist or Passwork too Short")

# Homepage get
@app.route('/home')
def home():
    return flask.render_template('home.html')

# Homepage Post
@app.route('/home', methods=['POST'])
def handle_home():
    return flask.render_template('home.html')

# DetailPage get
@app.route('/detail')
def home():
    return 'Detail'

# DetailPage Post
@app.route('/detail', methods=['POST'])
def handle_home():
    return 'Detail'

# NewOrder get
@app.route('/newOrder')
def home():
    return 'NewOrder'

# NewOrder Post
@app.route('/newOrder', methods=['POST'])
def handle_home():
    return 'NewOrder'

if __name__ == '__main__':
    app.run(debug=True, port=config.PORT)