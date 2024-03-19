from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.Ryans import Ryan
from flask_app.models.Accounts import Accounts
from flask import flash
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def only_ryans_home():
    return render_template('index.html')

@app.route('/register_ryan/push', methods=['POST'])
def save_ryan():
    form = request.form
    if Ryan.brian_check(form):
        return redirect('/')
    if not Ryan.ryan_name_check(form):
        return redirect('/')
    if not Ryan.validate_register(form):
        return redirect('/')
    if Ryan.registered_ryan(form):
        return redirect('/')
    
    pw_has = bcrypt.generate_password_hash(form['password'])
    
    register_data = {
        'ryan_name': form['ryan_name'],
        'last_name': form['last_name'],
        'email': form['email'],
        'password': pw_has
    }
    id = Ryan.save_ryan(register_data)
    Accounts.create_account(id)
    account = Ryan.login_ryan(register_data)
    session['user_id'] = id
    session['full_name'] = account['first_name'] +' '+ account['last_name']
    return redirect ('/dashboard')


# Log in routes
@app.route('/loginryan/push', methods=['POST'])
def login_ryan():
    if not Ryan.validate_login(request.form):
            return redirect('/')
    
    form = request.form
    login_info = {
        'email': form['email']
    }
    account = Ryan.login_ryan(login_info)
    if not account:
        Ryan.invalid_account()
        return redirect('/')
    
    pass_check = bcrypt.check_password_hash(account['password'],request.form['password'])

    if not pass_check:
        Ryan.invalid_account()
        return redirect('/')
    
    session['user_id'] = account['user_id']
    session['full_name'] = account['first_name'] +' '+ account['last_name']
    return redirect('/dashboard')

@app.route('/logout')
def login_out():
    session.clear()
    return redirect('/')