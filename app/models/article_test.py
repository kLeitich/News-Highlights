import unittest
from models import article
Article=article.Article

class Articletest(unittest.TestCase):
    def setUp(self):
        self.new_article=Article("The Wall Street Journal","Stephen Kalin, Summer Said and Warren P. Strobel","William Burns made an unannounced trip to Saudi Arabia last month, U.S. and Saudi officials said, with the relationship between Washington and Riyadh at its lowest point in decades.",'https://www.wsj.com/articles/cia-chief-met-saudi-crown-prince-last-month-in-push-to-mend-ties-11651588201','https://images.wsj.net/im-536339/social',"2022-05-03T15:07:39Z","DUBAICIA Director William Burns made an unannounced trip to Saudi Arabia last month to meet with Crown Prince Mohammed bin Salman, U.S. and Saudi officials said, as the Biden administration pushes to… [+390 chars]")
    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))


if __name__ == '__main__':
    unittest.main()
