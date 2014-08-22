#!/usr/bin/env python
import webapp2
from webapp2 import RequestHandler
from api import readdata, date_compare, TS_to_date, conform_output_data
import json


class AbstractPageHandler(RequestHandler):
    DATA_FILE = 'dataset.csv'
    API_DATA = readdata(filename=DATA_FILE)


class HomeHandler(AbstractPageHandler):

    def get(self):
        HOMEPAGE_HTML = 'A simple JSON API based on a CSV file.' \
                '<ul><li><a href="/api">The JSON API</a></li>' \
                '<li><a href="/csv">Download the CSV</a></li>' \
                '<li><a href="https://github.com/julzhk/simple_api">The code (github)</a></li>' \
                '</ul>'
        self.response.write(HOMEPAGE_HTML)

class CSVHandler(AbstractPageHandler):

    def get(self):
        """
            Provide the file as a download
        """
        self.response.headers['Content-Type'] = 'text/csv'
        with open(self.DATA_FILE, 'rb') as f:
            self.response.out.write(f.read())


class APIHandler(AbstractPageHandler):
    def get(self):
        """
        Provide the CSV data as a JSON Feed. Filter by show before/after date & show only some columns:
        - api?before=2014-01-13 13:31:00
        - api?after=2014-01-13
        - api?showcols=Symbol,LowPx,TradeCount
        - or a combination of any of these
        """
        before = TS_to_date(self.request.get('before', ''))
        after = TS_to_date(self.request.get('after', ''))
        cols = self.request.get('showcols', '')
        data = date_compare(self.API_DATA,
                            after_date=after,
                            before_date=before)
        data = [conform_output_data(d,cols) for d in data]
        self.response.write(json.dumps(data))


app = webapp2.WSGIApplication([
    ('/', HomeHandler),
    ('/csv', CSVHandler),
    ('/.+', APIHandler)
], debug=True)
