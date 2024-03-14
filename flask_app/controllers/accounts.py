from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.Ryans import Ryan
from flask_app.models.Accounts import Accounts
from flask import flash

@app.route('/profile')
def jump_to_profile():
    user_id = session['user_id']
    user = Ryan.ryan_details(user_id)
    return render_template('profile.html',ryan=user)

@app.route('/accounts')
def jump_to_accounts():
    if not session['user_id']:
        return redirect('/')
    user_id = session['user_id']
    details = Accounts.get_saved_accounts(user_id)
    return render_template('socialmedia.html', accounts = details)

@app.route('/account/push', methods =['POST'])
def save_to_account():
    form = request.form
    print(form)
    data = {
        'user_id': form['user_id'],
        'facebook': form['facebook'],
        'instagram': form['instagram'],
        'snapchat': form['snapchat'],
        'twitter': form['twitter']
    }
    action = request.form.get('action')
    if action == 'Update':
        Accounts.update_accounts(data)
    elif action == 'Save':
        Accounts.save_accounts(data)
    return redirect('/profile')