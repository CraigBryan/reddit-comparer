import json
from reddit_entry import RedditComment
from reddit_entry import RedditPost

class RedditUser(object):
  """
  Represents a reddit user by the information provided by the .json link.
  """

  def __init__(self, name, raw_data):
    """
    Stores the user name and decodes the JSON
    """
    self.name = name
    self.data = json.loads(raw_data)
   
  def pretty_print_history(self):
    print json.dumps(self.data, indent=2, sort_keys=True) 

  def get_latest_post(self):
    """
    Returns the data from the most recent post by this user.
    This uses the reddit type system to determine whether an entry is a post 
    or comment. "t1" is a comment, "t3" is a post.
    """

    for entry in self._get_user_entries():
      if entry["kind"] == "t3":
        return RedditPost(entry["data"])
 
    return None

  def get_latest_comment(self):
    """
    Returns the data from the most recent comment by this user.
    This uses the "title" attribute to distinguish between comments and posts.
    """

    for entry in self._get_user_entries():
      if entry["kind"] == "t1":
        return RedditComment(entry["data"])

    return None

  def print_name(self):
    """
    Simple string representation that gives the user name
    """

    return "Data for Reddit user: %s" % self.name

  def __str__(self):
    return json.dumps(self.data)

  def _get_user_entries(self):
    return self.data['data']['children']