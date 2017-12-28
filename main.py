from flask import Flask, render_template, request, redirect
import re



app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template("index.html", title="Main Page")

@app.route("/signup", methods=['POST', 'GET'])
def signup():
    username =''
    email =''

    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    name_error =''
    password_error =''
    verify_error =''
    email_error =''

    #if username == '' or ' ' in username or len(username) > 20 or len(username) <3:
    if not re.fullmatch('\S{3,20}', username):
        name_error = "That is not a valid username!"
        
    if password == '' or ' ' in password or len(password) > 20 or len(password) <3:
        password_error = "That is not a valid password!"
        
    if verify != password:
        verify_error = "Passwords don't match!"

    if ' ' in email or len(email) > 20 or len(email) < 3 or "@" not in email or "." not in email:
        email_error = "That is not a valid email!"

    if name_error or password_error or verify_error or email_error:
        return render_template("index.html", username=username, email=email, name_error=name_error, password_error=password_error, 
                                        verify_error=verify_error, email_error=email_error)
    else:
        return render_template("welcome.html", username=username)
    
    

app.run()