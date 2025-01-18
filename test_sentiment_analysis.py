from SentimentAnalysis.sentiment_analysis import sentiment_analyzer
import unittest


class TestSentimentAnalyzer(unittest.TestCase):
    def test_sentiment_analyzer(self):
        """
        test 
        """
        #1.  case  1
        reponse_1 =sentiment_analyzer("I love working with Python")
        self.assertEqual(reponse_1['label'] ,"SENT_POSITIVE")

        #2. case 
        result_2 =sentiment_analyzer('I hate working with Python')
        self.assertEqual(result_2['label'], 'SENT_NEGATIVE')

        # Test case for neutral sentiment
        result_3 = sentiment_analyzer('I am neutral on Python')
        self.assertEqual(result_3['label'], 'SENT_NEUTRAL')

unittest.main()