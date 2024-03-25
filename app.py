from flask import Flask, render_template, request
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        amount = request.form['amount']
        converted_amount = convert_usd_to_inr(amount)
        return render_template('index.html', converted_amount=converted_amount)
    return render_template('index.html')

def convert_usd_to_inr(amount):
    api_url = 'https://api.exchangerate-api.com/v4/latest/USD'
    response = requests.get(api_url)
    data = response.json()
    exchange_rate = data['rates']['INR']
    converted_amount = float(amount) * exchange_rate
    return converted_amount

if __name__ == '__main__':
    app.run(debug=True)
