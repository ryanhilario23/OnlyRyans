from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.Postings import Posting
from flask_app.models.Ryans import Ryan

@app.route('/dashboard')
def onlyRyans_home():
    if not session:
        return redirect('/')
    


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

@app.route('/view/<int:user_id>')
def see_ryan(user_id):
    user = Ryan.ryan_details(user_id)
    return render_template('profile.html',ryan=user)

@app.route('/likes_<int:post_id>')
def ryan_like_this(post_id):
    data ={
        'user_id': session['user_id'],
        'post_id': post_id
    }
    Posting.ryan_likes(data)
    return redirect('/dashboard')


@app.route('/view_post/<int:post_id>')
def jump_to_post(post_id):
    post = Posting.view_post(post_id)
    ryans = Ryan.who_likes_this(post_id)
    print(ryans)
    return render_template('read_post.html', table = ryans, post=post)

@app.route('/delete_post/<int:post_id>')
def delete_post(post_id):
    Posting.delete_likes(post_id)
    Posting.delete_post(post_id)
    return redirect('/dashboard')