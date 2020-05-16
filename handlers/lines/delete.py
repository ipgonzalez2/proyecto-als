# coding: utf-8
# New song
import webapp2
import time
from webapp2_extras import jinja2

from model.line import Line
from webapp2_extras.users import users

class DeleteHandler(webapp2.RequestHandler):

    def get(self):
        usr = users.get_current_user()
        line = Line.get(self.request)
        if usr:
            line.key.delete()
            time.sleep(1)
            return self.redirect("/")

        else:
            return self.redirect("/")


app = webapp2.WSGIApplication([
    ('/lines/delete', DeleteHandler)
], debug=True)
