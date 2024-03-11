from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.Ryans import Ryan
from flask import flash
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def only_ryans_home():
    return render_template('index.html')


# Log in routes
@app.route('/loginryan/push', methods=['POST'])
def login_ryan():
    if Ryan.validate_login(request.form):
            return redirect('/')
    
    form = request.form
    login_info = {
        'email': form['email'],
        'password': form['password'] 
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
    return  redirect('/dashboard')

@app.route('/dashboard')
def logged_in_ryan():
    if not session['user_id']:
        return redirect('/')





#Register the Ryan name
@app.route('/register_ryan')
def jump_ryan():
    return render_template('registerRyan.html')

@app.route('/register_ryan/push', methods=['POST'])
def register_ryan():
    form = request.form
    if not Ryan.validate_name(form):
        return redirect('/register_ryan')
    if not Ryan.brian_check(form):
        return redirect('/register_ryan')
    
    data ={
        'name': form['ryan_name'],
        'email': form['email']
    }
    Ryan.submit_ryan_entry(data)
    flash('Your Ryan name has been submitted.', 'ryan_register')
