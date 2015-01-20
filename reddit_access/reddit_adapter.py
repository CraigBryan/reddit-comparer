import urllib2
from reddit_user import RedditUser

class RedditAdapter(object):
  """
  A simple adapter that is responsible for grabbing data from the reddit server
  """

  def get_user(self, username):
    """
    Returns the .json data from reddit about that user
    """

    url = 'http://www.reddit.com/user/%s.json' % username
    data = urllib2.urlopen(url).read()

    if data == '{"error": 404}':
      raise AttributeError("No such user found")
    else:
      return RedditUser(username, data)