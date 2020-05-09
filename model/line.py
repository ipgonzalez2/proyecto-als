# Song

from google.appengine.ext import ndb

class Line(ndb.Model):
    title = ndb.StringProperty(required=True)
    artist = ndb.StringProperty(required=True)
    line = ndb.StringProperty(required=True)
    email = ndb.StringProperty(required=True, indexed=True)
