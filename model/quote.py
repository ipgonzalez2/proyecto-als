# Quote

from google.appengine.ext import ndb
from song import Song
from user import User

class Quote(ndb.Model):
    song = ndb.KeyProperty(kind=Song)
    user = ndb.KeyProperty(kind=User)
    line = ndb.StringPropery(required=True)