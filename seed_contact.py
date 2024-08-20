from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__ , static_folder='static')
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = '<your email address>' #The email for sending others details
app.config['MAIL_PASSWORD'] = 'password' #make sure to turn on less secure app access in your gmail settings
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

@app.route('/', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        msg = Message(subject='Contact Form Submission',
                      sender=email,
                      recipients=['email'], #The email you wish to receive the details of others
                      body=f"Name: {name}\nEmail: {email}\nMessage: {message}")

        mail.send(msg)
        return 'Message sent!'

    return render_template('Home.html')

if __name__ == '__main__':
    app.run(debug=True)