from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)
config_file = 'config.txt'

def load_config():
    config = {}
    try:
        with open(config_file, 'r') as file:
            for line in file:
                key, value = line.strip().split('=')
                config[key] = value
        print("Configuration loaded.")
    except FileNotFoundError:
        print("Configuration file not found.")
    except Exception as e:
        print(f"Error loading configuration: {e}")
    return config

def save_config(email, phone, password, account_sid):
    try:
        with open(config_file, 'w') as file:
            file.write(f"email={email}\n")
            file.write(f"phone={phone}\n")
            file.write(f"password={password}\n")
            file.write(f"account_sid={account_sid}\n")
        print("Configuration saved.")
    except Exception as e:
        print(f"Error saving configuration: {e}")

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email_phone = request.form.get('email_phone')
        password = request.form.get('password')

        config = load_config()
        stored_email = config.get('email', '')
        stored_phone = config.get('phone', '')
        stored_password = config.get('password', '')

        if (email_phone == stored_email or email_phone == stored_phone) and password == stored_password:
            return redirect(url_for('welcome', email=stored_email, phone=stored_phone))
        else:
            error_message = "Invalid email/phone or password."
            return render_template('login.html', error_message=error_message)

    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        phone = request.form.get('phone')
        password = request.form.get('password')
        account_sid = request.form.get('account_sid')

        save_config(email, phone, password, account_sid)
        return redirect(url_for('login'))

    return render_template('signup.html')

@app.route('/welcome')
def welcome():
    email = request.args.get('email')
    phone = request.args.get('phone')
    return render_template('welcome.html', email=email, phone=phone)

if __name__ == '__main__':
    app.run()
