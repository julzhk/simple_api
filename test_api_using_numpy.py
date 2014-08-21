import unittest
import numpy as np
import datetime

COLUMN_LABELS = ['Name', 'Value', 'TimeStamp']

def str2datetime(s):
 return datetime.datetime.strptime(s[:19], "%Y-%m-%d %I:%M:%S")


class TestAPIFunctions(unittest.TestCase):

    def setUp(self):
        self.df = np.loadtxt('test_dataset.csv',
                        skiprows=1,
                        dtype={'names': COLUMN_LABELS,
                               'formats': ['S8','I8','S19']},
                        delimiter=',')


    def test_simple_numpy(self):
        self.assertEqual( self.df[0][0],'name1')
        self.assertEqual( self.df[0][1],1)
        self.assertEqual( self.df[1][0],'name2')
        self.assertEqual( self.df[1][1],2)

    def test_dates(self):
        testdate = str2datetime(self.df[0][2])
        self.assertEqual(testdate,
                         datetime.datetime.strptime(
                             '2013-07-19 08:47:00', "%Y-%m-%d %I:%M:%S")
                        )


    def test_one_where_clause(self):
        r = np.where(self.df['TimeStamp'] > '2013-07-22 09:48')
        print [self.df[i] for i in r]

if __name__ == '__main__':
    unittest.main()