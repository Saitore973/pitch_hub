from flask import render_template,request,redirect,url_for
from . import main
from .forms import PitchForm
from flask_login import login_required, current_user
from ..models import  Pitch
from .. import db
@main.route('/')
def index():
    return render_template('index.html')

@main.route("/home")
def home():
    return render_template('home.html')

@main.route('/pitches', methods = ['GET','POST'])
@login_required
def pitches(id):
    form = PitchForm()
    
    if form.validate_on_submit():
      pitch = Pitch(pitch =form.pitch.data, name = form.name.data)
      db.session.add(pitch)
      db.session.commit()
      return redirect(url_for('.pitches'))
    posts = Pitch.query.all()
    return render_template('pitches.html', posts =posts , pitches = pitches, pitch_form = form)
