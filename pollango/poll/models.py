from google.appengine.ext import db
from django import newforms as forms



class User(db.Model):
    id = db.StringProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)
    updated = db.DateTimeProperty(auto_now=True)
    name = db.StringProperty(required=True)
    profile_url = db.StringProperty(required=True)
    access_token = db.StringProperty(required=True)

class Poll(db.Model):
    question = db.StringProperty()
    created_on = db.DateTimeProperty(auto_now_add = 1)
    created_by = db.UserProperty()
    
    def __str__(self):
        return '%s' %self.question
    
    def get_absolute_url(self):
        return '/poll/%s/' % self.key()
    
    
class Choice(db.Model):
    poll = db.ReferenceProperty(Poll)
    choice = db.StringProperty()
    votes = db.IntegerProperty(default = 0)

class Answer(db.Model):
	choice = db.ReferenceProperty(Choice)
	user = db.ReferenceProperty(User)
	submitted = db.DateTimeProperty(auto_now_add=True)
