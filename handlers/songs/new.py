# coding: utf-8
# New song
import webapp2
import time
from webapp2_extras import jinja2

from model.song import Song

class NewSongHandler(webapp2.RequestHandler):
    def get(self):


        values_template= {

        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("newSong.html", **values_template))

    def post(self):
        title = self.request.get("edTitle", "")
        artist = self.request.get("edArtist", "")
        link = self.request.get("edLink","")


        if not(title) or not(artist) or not(link):
            return self.redirect("/")
        else:
            song = Song(title=title, artist=artist, link=link)
            song.put()
            time.sleep(1)
            return self.redirect("/")


app = webapp2.WSGIApplication([
    ('/songs/new', NewSongHandler)
], debug=True)
