This is a simple REST web API in Python & Google App Engine to retrieve data from the provided data set in CSV

The users of this API can specify a range of timestamps
and optionally name which columns they are interested in.

The API returns the relevant data in a JSON format.

---
SIMPLE USES
## http://127.0.0.1:8080/api
This returns all of the data from the datafile
## http://127.0.0.1:8080/api?before=2014-01-13
This returns data after the date set (in this case before the 13th Jan 2014)
## http://127.0.0.1:8080/api?after=2010-02-20
This returns data after the date set (in this case before the 20th Feb 2010)
## http://127.0.0.1:8080/api?before=2014-01-13&after=2010-02-20
This returns data combines both filters


MORE PRECISE:
## http://127.0.0.1:8080/api?before=2014-01-13 13:31:00
This filters only data that's before 13th Jan 2014 1:31pm


FILTERING FIELDS
##http://127.0.0.1:8080/api?showcols=Symbol,LowPx,TradeCount
This returns just the Symbol,LowPx,TradeCount fields.


A MORE COMPLEX REQUEST
All of the options can be used simultaneously:
http://127.0.0.1:8080/api?before=2051-01-01 01:01:01&after=2013-07-21&showcols=Symbol,LowPx,TradeCount

TESTS
The project used test driven development to make sure it was on the right track.

FUTURE DEVELOPMENT
If there was more complex data or requirements I'd consider using Numpy to manipulate & hold the data array.
Hence the test_numpy.py file sketching out this direction.

Similarly a simple memcache decorator can be added if there was any load. But as the data isn't from a database, it's
probably not useful. (see memcache_decorator.py)