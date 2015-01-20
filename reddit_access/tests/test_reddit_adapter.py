import unittest
from urllib2 import HTTPError
from ..reddit_adapter import RedditAdapter

class TestRedditAdapter(unittest.TestCase):
  
  def setUp(self):
    self.adapter = RedditAdapter()

  def test_get_empty_user(self):
    user = "Empty"
    expected = '{"kind": "Listing", "data": {"modhash": "", "children": [], "after": null, "before": null}}'

    actual = self.adapter.get_user(user).__str__()

    self.assertEqual(actual, expected)

  def test_get_non_existant_user(self):
    user = ";"

    with self.assertRaises(HTTPError):
      self.adapter.get_user(user)