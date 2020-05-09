# coding: utf-8
# New song
import webapp2
import time
from webapp2_extras import jinja2

from model.line import Line
from webapp2_extras.users import users

class DeleteHandler(webapp2.RequestHandler):

    def post(self):
        usr = users.get_current_user()

        if usr:
            title = self.request.get("edTitle", "")
            artist = self.request.get("edArtist", "")
            line = self.request.get("edLine","")


            if not(title) or not(artist) or not(line):
                return self.redirect("/")
            else:
                line = Line(title=title, artist=artist, line=line, email=usr.email())
                line.put()
                time.sleep(1)
                return self.redirect("/")

        else:
            return self.redirect("/")


app = webapp2.WSGIApplication([
    ('/lines/delete', DeleteHandler)
], debug=True)
