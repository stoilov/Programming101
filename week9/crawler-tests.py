from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from connect import Base
from crawler import Crawler

import unittest


class CrawlerTest(unittest.TestCase):
    def setUp(self):
        engine = create_engine("sqlite:///search.db")
        Base.metadata.create_all(engine)
        session = Session(bind=engine)

        self.crawler = Crawler(session)

    def test_is_out_going_not_out_going(self):
        is_outgoing = self.crawler.is_outgoing('http://hackbulgaria.com', 'http://hackbulgaria.com/about/') 
        self.assertFalse(is_outgoing)

    def test_is_out_going_is_out_going(self):
        is_outgoing = self.crawler.is_outgoing('http://hackbulgaria.com', 'http://facebook.com/about/') 
        self.assertTrue(is_outgoing)

    def test_is_out_going_subdomain(self):
        is_outgoing = self.crawler.is_outgoing('http://hackbulgaria.com', 'http://blog.hackbulgaria.com/') 
        self.assertTrue(is_outgoing)

    def test_can_be_scanned_hashtag(self):
        can_be_scanned = self.crawler.can_be_scanned('http://hackbulgaria.com#da', 'http://hackbulgaria.com/')
        self.assertFalse(can_be_scanned)

    def test_can_be_scanned_no_hashtag(self):
        can_be_scanned = self.crawler.can_be_scanned('http://hackbulgaria.com/about/', 'http://hackbulgaria.com/')
        self.assertTrue(can_be_scanned)

    def test_can_be_scanned_double(self):
        can_be_scanned1 = self.crawler.can_be_scanned('http://hackbulgaria.com/about/', 'http://hackbulgaria.com/')
        self.crawler.visited.append('http://hackbulgaria.com/about/')
        can_be_scanned2 = self.crawler.can_be_scanned('http://hackbulgaria.com/about/', 'http://hackbulgaria.com/')

        self.assertTrue(can_be_scanned1)
        self.assertFalse(can_be_scanned2)


if __name__ == '__main__':
    unittest.main()