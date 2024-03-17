from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.Postings import Posting
from flask_app.models.Ryans import Ryan

@app.route('/dashboard')
def onlyRyans_home():
    if not session['user_id']:
        return redirect('/')
    id = session['user_id']
    list = Ryan.show_all_post()

    print(session['full_name'])
    return render_template('dashboard.html',ryans=list)

@app.route('/create_post', methods=['POST'])
def save_post():
    form = request.form
    data ={
        'user_id': form['user_id'],
        'post': form['post']
    }
    Posting.create_post(data)
    return redirect('/dashboard')


@app.route('/likes_<int:post_id>')
def ryan_like_this(post_id):
    data ={
        'user_id': session['user_id'],
        'post_id': post_id
    }
    Posting.ryan_likes(data)
    return redirect('/dashboard')