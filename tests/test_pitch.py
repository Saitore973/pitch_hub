from unicodedata import name
from app.models import Pitch,User
from app import db

def setUp(self):
        self.user_James = User(username = 'Admin',password = '1234', email = 'admin@gmail.com')
        self.new_review = Pitch(user_id=12345,name='pitch name',pitch='This pitch is the best thing since sliced bread', )

def tearDown(self):
        Pitch.query.delete()
        User.query.delete()

def test_check_instance_variables(self):
        self.assertEquals(self.new_pitch.user_id,12345)
        self.assertEquals(self.new_pitch.name, 'pitch name')
        self.assertEquals(self.new_pitch.pitch, 'This pitch is the best thing since sliced bread' )

def test_save_review(self):
        self.new_review.save_review()
        self.assertTrue(len(Pitch.query.all())>0)  

def test_get_review_by_id(self):

        self.new_review.save_review()
        got_reviews = Pitch.get_reviews(12345)
        self.assertTrue(len(got_reviews) == 1)     