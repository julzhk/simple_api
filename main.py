#!/usr/bin/env python
#
import webapp2
from api import readdata, date_compare, TS_to_date, conform_output_data
DATA_FILE = 'dataset.csv'
import json


class MainHandler(webapp2.RequestHandler):
    API_DATA = readdata(filename=DATA_FILE)

    def get(self):
        before = TS_to_date(self.request.get('before', ''))
        after = TS_to_date(self.request.get('after', ''))
        cols = self.request.get('showcols', '')
        data = date_compare(self.API_DATA,
                            after_date=after,
                            before_date=before)
        data = [conform_output_data(d,cols) for d in data]
        self.response.write(json.dumps(data))


app = webapp2.WSGIApplication([
    ('/api', MainHandler)
], debug=True)
