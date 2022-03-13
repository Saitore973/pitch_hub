from flask import render_template,request,redirect,url_for,abort
from . import main
from .forms import PitchForm,UpdateProfile
from flask_login import login_required, current_user
from ..models import  Pitch,User, Dislikes, Likes
from .. import db,photos
import markdown2
@main.route('/')
def index():
    return render_template('index.html')

@main.route("/home")
def home():
    return render_template('home.html')


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/pitches', methods = ['GET','POST'])
@login_required
def pitches():
    form = PitchForm()
    
    if form.validate_on_submit():
      pitch = Pitch(pitch =form.pitch.data, name = form.name.data)
      db.session.add(pitch)
      db.session.commit()
      return redirect(url_for('.pitches'))
    posts = Pitch.query.all()
    return render_template('pitches.html', posts =posts , pitches = pitches, pitch_form = form)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)


@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))


@main.route('/like/<int:id>',methods = ['POST','GET'])
@login_required
def like(id):
    get_pitches = Likes.get_likes(id)
    valid_string = f'{current_user.id}:{id}'
    for pitch in get_pitches:
        to_str = f'{pitch}'
        print(valid_string+" "+to_str)
        if valid_string == to_str:
            return redirect(url_for('main.pitches',id=id))
        else:
            continue
    new_vote = Likes(user=current_user, pitch_id=id)
    new_vote.save()
    return redirect(url_for('main.pitches',id=id))


@main.route('/dislike/<int:id>',methods = ['POST','GET'])
@login_required
def dislike(id):
    get_pitches = Dislikes.get_dislikes(id)
    valid_string = f'{current_user.id}:{id}'
    for pitch in get_pitches:
        to_str = f'{pitch}'
        print(valid_string+" "+to_str)
        if valid_string == to_str:
            return redirect(url_for('main.pitches',id=id))
        else:
            continue
    new_vote = Dislikes(dislike=current_user, pitch_id=id)
    new_vote.save()
    return redirect(url_for('main.pitches',id=id))