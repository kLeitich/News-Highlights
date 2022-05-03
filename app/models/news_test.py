import unittest
from models import news
News=news.News

class Newstest(unittest.TestCase):
    def setUp(self):
        self.new_news=News("abcnews",'News is just awesome to see','a new way to see it','https://abcnews.go.com/','general','en','us')
    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))


if __name__ == '__main__':
    unittest.main()
