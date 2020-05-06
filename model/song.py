# Song

from google.appengine.ext import ndb

class Song(ndb.Model):
    title = ndb.StringProperty(required=True)
    artist = ndb.StringProperty(required=True)
    link = ndb.StringProperty(required=True)
