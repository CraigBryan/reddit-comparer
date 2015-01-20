import unittest
from ..reddit_user import RedditUser

class TestRedditUser(unittest.TestCase):
  
  def setUp(self):
    self.test_user = RedditUser("test_user", self._example_json())
    self.test_empty_user = RedditUser("test_user", self._empty_example_json())

  def test_get_latest_post(self):
    expected = self.test_user.get_latest_post().__str__()
    actual = "example comment"

    self.assertEqual(actual, expected)
    
  def test_get_latest_comment(self):
    expected = self.test_user.get_latest_comment().__str__()
    actual = "example post"

    self.assertEqual(actual, expected)

  def test_print_name(self):
    expected = self.test_user.print_name()
    actual = "Data for Reddit user: test_user"

    self.assertEqual(actual, expected)

  def test_empty_latest_post(self):
    expected = self.test_empty_user.get_latest_post()

    self.assertIsNone(expected)

  def test_empty_latest_comment(self):
    expected = self.test_empty_user.get_latest_comment()

    self.assertIsNone(expected)

  def _example_json(self):
    data = '''{
                "data": {
                  "children": [
                    {
                      "data": "example comment", 
                      "kind": "t3"
                    },
                    {
                      "data": "example post",
                      "kind": "t1"
                    }
                  ]
                }
              }'''
    return data

  def _empty_example_json(self):
    data = '''{
                "data": {
                  "children": []
                }
              }'''
    return data