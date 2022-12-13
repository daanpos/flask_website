from flask import Blueprint, render_template, request, redirect, url_for, flash


auth = Blueprint('auth', __name__)

users = {'daanpos005@gmail.com': '1234567',
        'hallo@hotmail.com': 'hallo.nl123',
        'daniel.pos@hva.nl': 'Lamp1234!',
        'hallo': '123'
        }

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form.get('user')
        password = request.form.get('password')
        print(user)
        print(password)

        if user in users:
            if users[user] == password:
                print(users[user], password)
                return redirect(url_for('views.multimedia'))
            else:
                return "Password is incorrect."
        else:
            return "User is not in database."
            
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "<p>logout</p>"

@auth.route('/sign-in')
def sign_in():
    return "<p>sign-in</p>"

