import flask
import src.db as db
import config

app = flask.Flask(__name__)
app.secret_key = "super secret key"
cur_user = None

db.init_db(app)

# Index get
@app.route('/')
def index():
    return flask.redirect('/login')

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
        flask.session['user'] = user.get('username')
        print("Current User: " + flask.session['user'])
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
        flask.session['user'] = user.get('username')
        print("Current User: " + flask.session['user'])
        return flask.redirect('/home')

    return flask.render_template('register.html', message="Username Already Exist or Passwork too Short")

# Logout
@app.route('/logout')
def logout():
    flask.session.clear()
    return flask.redirect('/login')

# Homepage get
@app.route('/home')
def home():
    if 'user' not in flask.session:
        return flask.redirect('/login')
    user = flask.session['user']
    print("Current User: " + user)
    customer = db.find_user_order(user)
    order_ids = []
        
    return flask.render_template('home.html', user=user)

# Homepage Post
@app.route('/home', methods=['POST'])
def handle_home():
    return flask.render_template('home.html')

# DetailPage get
@app.route('/detail/<order_id>')
def detail(order_id): 
    order = db.get_order(order_id)
    return flask.render_template('detail.html', order=order)

# DetailPage Post
@app.route('/detail/<order_id>/save', methods=['POST'])
def handle_detail(order_id):
    order = db.get_order(order_id)
    updated_data = {
        "customer_name": flask.request.form.get("customerName"),
        "dish_name": flask.request.form.get("dishName"),
        "price": float(flask.request.form.get("price")),  
        "address": flask.request.form.get("address")
    }
    db.update_order(order_id, updated_data)

    return flask.render_template('detail.html', order=order)

# NewOrder get
@app.route('/newOrder')
def order():
    return 'NewOrder'

# NewOrder Post
@app.route('/newOrder', methods=['POST'])
def handle_odrer():
    return 'NewOrder'

if __name__ == '__main__':
    consumer = "Hi"
    food = "Pizza"
    address = "123 Main Street",
    price = 19.99
    
    # db.create_user("Frank", '123456')

    # db.create_order("Frank", consumer, food, address, price)
    # s = db.find_user_order("Frank")
    # print(s)
    app.run(debug=True, port=config.PORT)

