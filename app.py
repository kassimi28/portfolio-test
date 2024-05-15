from flask import Flask, render_template, request, redirect, session, url_for
import requests
import random
import sys

app = Flask(__name__)
app.secret_key = 'your_secret_key'

reload(sys)
sys.setdefaultencoding('utf-8')

# Function to fetch product details by ID
def get_product_details(product_id):
    url = "https://makeup-api.herokuapp.com/api/v1/products/{}.json".format(product_id)
    response = requests.get(url)
    product = response.json()
    return product

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/elements')
def elements():
    return render_template('elements.html')

@app.route('/selection')
def selection():
    # Fetch data from the API
    url = "https://makeup-api.herokuapp.com/api/v1/products.json?brand=covergirl&product_type=lipstick"
    response = requests.get(url)
    products = response.json()

    return render_template('home.html', products=products)

@app.route('/product/<int:product_id>')
def product_details(product_id):
    # Fetch product details
    product = get_product_details(product_id)
    return render_template('card.html', product=product)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Dummy authentication with dummyjson.com
        login_url = "https://dummyjson.com/auth/login"
        data = {'username': username, 'password': password}
        response = requests.post(login_url, data=data)
        if response.status_code == 200:
            session['username'] = username
            return redirect(url_for('index'))
        else:
            return render_template('login.html', error='Invalid username or password')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
