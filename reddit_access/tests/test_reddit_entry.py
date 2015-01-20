import unittest
from ..reddit_entry import RedditEntry

class TestRedditEntry(unittest.TestCase):
  
  def setUp(self):
    self.test_entry = RedditEntry(self._example_data())

  def test_empty_user(self):
    with self.assertRaises(AttributeError):
      RedditEntry(None)

  def test_get_score(self):
    expected = self.test_entry.get_score()
    actual = 123

    self.assertEqual(actual, expected)

  def _example_data(self):
    return {"score": 123}
