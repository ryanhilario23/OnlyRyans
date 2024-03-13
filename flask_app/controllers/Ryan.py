from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.Ryans import Ryan
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
    if not Ryan.validate_register(form):
        return redirect('/')
    if not Ryan.ryan_name_check(form):
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
    session['user_id'] = id
    return redirect ('/dashboard')

@app.route('/dashboard')
def onlyRyans_home():
    if not session['user_id']:
        return redirect('/')
    id = session['user_id']
    user = Ryan.get_user(id)
    session['full_name'] = user['first_name'] +' '+ user['last_name']
    print(session['full_name'])
    return render_template('dashboard.html',ryan=user)

@app.route('/profile/<int:user_id>')
def jump_to_profile(user_id):
    user = Ryan.get_user(user_id)
    return render_template('profile.html',ryan=user)


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
    return redirect('/dashboard')

@app.route('/dashboard')
def logged_in_ryan():
    if not session['user_id']:
        return redirect('/')





#Register the Ryan name
@app.route('/register_ryan')
def jump_ryan():
    return render_template('registerRyan.html')

@app.route('/register_ryan_name/push', methods=['POST'])
def register_ryan():
    form = request.form
    data ={
        'name': form['ryan_name'],
        'email': form['email']
    }

    if not Ryan.validate_name(data):
        return redirect('/register_ryan')
    if Ryan.brian_check(data):
        return redirect('/register_ryan')
    
    Ryan.submit_ryan_entry(data)
    flash('Your Ryan name has been submitted.', 'ryan_register')


@app.route('/logout')
def login_out():
    session.clear()
    return redirect('/')