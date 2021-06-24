import unittest
import pandas as pd
import sys, os
sys.path.append(os.path.abspath(os.path.join('..')))

from clean_tweets_dataframe import Clean_Tweets

from extract_dataframe import read_json
from extract_dataframe import TweetDfExtractor
_, tweet_list = read_json("./data/covid19.json")

class TestCleanTweetsDataframe(unittest.TestCase):
  def setUp(self) -> None:
      self.extracted_tweets = TweetDfExtractor(tweet_list[:5])
      self.df = self.extracted_tweets.get_tweet_df()
      self.tweet_list = Clean_Tweets(self.df)
  
  def test_class_working(self):
    self.assertIsNotNone(self.tweet_list)

  def test_drop_unwanted_column(self):
    # columns = ["created_at"]
    
    pass

  def test_drop_duplicate(self):
    print('text drop duplication')
    pass

  def test_convert_to_datetime(self):
    pass

  def test_convert_to_numbers(self):
    pass

  def test_remove_non_english_tweets(self):
    pass


  
if __name__ == '__main__':
	unittest.main()
