#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
from webapp2_extras import jinja2
from model.line import Line
from webapp2_extras.users import users


class ListHandler(webapp2.RequestHandler):
    def get(self):
        usr = users.get_current_user()

        if usr:
            url_usr = users.create_logout_url("/")
            lines = Line.query(Line.email == usr.email())
            linesOthers = Line.query(Line.email != usr.email()
                                     )
            quotes = []

            for l in lines:
                quotes.append(l.line.lower())

            linesNew = []

            for line in linesOthers:
                if line.line.lower() not in quotes:
                    linesNew.append(line)


        else:
            url_usr = users.create_login_url("/")
            linesNew =[]

        print(linesNew)
        values_template = {
            "lines": linesNew,
            "usr": usr,
            "url_usr": url_usr
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("list.html", **values_template))

app = webapp2.WSGIApplication([
    ('/lines/list', ListHandler)
], debug=True)
