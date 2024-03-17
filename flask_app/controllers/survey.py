from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.Ryans import Ryan
from flask_app.models.Survey import Survey
from flask import flash
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/register_ryan')
def jump_ryan_entry():
    return render_template('registerRyan.html')

@app.route('/register_ryan_name/push', methods=['POST'])
def register_ryan():
    form = request.form
    data ={
        'ryan_name': form['ryan_name'],
        'email': form['email']
    }
    if Ryan.brian_check(data):
        print('brians?')
        return redirect('/register_ryan')
    if Survey.check_name_submitted(data):
        print('name')
        return redirect('/register_ryan')
    
    if not Survey.survey_email(data):
        print('email')
        return redirect('/register_ryan')
    Survey.submit_entry(data)
    return redirect('/register_ryan')


@app.route('/ryan_poll')
def jump_to_poll():
    data = Survey.view_all_entry()
    print(data)
    return render_template('ryanpoll.html', data = data)

@app.route('/cast_vote/push',methods=['POST'])
def ryan_voted():
    form = request.form
    data = {
        'entry_id': form['entry_id'],
        'vote': form['vote'],
        'user_id':form['user_id']
    }
    Survey.submit_vote(data)
    return redirect('/ryan_poll')