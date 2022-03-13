from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired



class PitchForm(FlaskForm):
    pitch = TextAreaField('Enter your Pitch')
    name = StringField('Enter your name', validators=[DataRequired()])
    submit = SubmitField('Pitch', validators=[DataRequired()])

class ReviewForm(FlaskForm):

 title = StringField('Review title',validators=[DataRequired()])

 review = TextAreaField('Movie review')

 submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
 bio = TextAreaField('Tell us about you.',validators = [DataRequired()])
 submit = SubmitField('Submit')