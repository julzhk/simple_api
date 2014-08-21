import unittest
import datetime
from api import readdata, DATA_FILE, date_compare


class TestAPIFunctions(unittest.TestCase):

    def setUp(self):
        self.data = readdata(filename=DATA_FILE)

    def test_simple_data_read(self):
        self.assertEqual(self.data[0]['Name'],'name1')
        self.assertEqual(self.data[1]['Name'],'name2')

    def test_coerce_data_types(self):
        self.assertEqual(self.data[0]['QuoteCount'], 1)
        self.assertEqual(self.data[1]['QuoteCount'], 2)
        self.assertEqual(self.data[1]['TimeStamp'],
                          datetime.datetime(2013, 7, 22, 8, 47))

    def test_compare_dates_to_rows_returns_all_data(self):
        after = date_compare(data=self.data,
                             after_date=datetime.datetime(2013, 1, 1, 0, 0))
        self.assertEqual(after, self.data)
        self.assertEqual(len(after), len(self.data))

    def test_compare_dates_to_rows_filters_after_data(self):
        after = date_compare(data=self.data,
                             after_date=datetime.datetime(2013, 7, 21, 0, 0))
        self.assertEqual(len(after), 2)
        self.assertEqual(after[0]['Name'],'name2')

    def test_compare_dates_to_rows_filters_before_data(self):
        before = date_compare(data=self.data,
                             before_date=datetime.datetime(2013, 7, 23, 0, 0))
        self.assertEqual(len(before), 2)
        self.assertEqual(before[0]['Name'],'name1')
        self.assertEqual(before[1]['Name'],'name2')



if __name__ == '__main__':
    unittest.main()