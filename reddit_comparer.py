from __future__ import print_function
from reddit_access.reddit_adapter import RedditAdapter
import sys

class RedditComparer(object):
  def __init__(self, usernames):
    self.reddit = RedditAdapter()

    self.users = [self.reddit.get_user(x) for x in usernames]

  def get_comparision_posts(self):
    comp = self._get_empty_comp("post")

    for user in self.users:
      try:
        comp['scores'].append((user.name, user.get_latest_post().get_score()))
      except AttributeError:
        comp["scores"].append((user.name, 0)) 

    return comp

  def get_comparision_comments(self):
    comp = self._get_empty_comp("comment")

    for user in self.users:
      try:
        comp["scores"].append((user.name, user.get_latest_comment().get_score()))
      except AttributeError:
        comp["scores"].append((user.name, 0)) 

    return comp

  def pretty_print_comparision(self, comp_dict):
    print("Recent submitted %s comparision\n" %comp_dict['type'])

    #sorts list of tuples by 2nd key (score in this case)
    comp_dict['scores'].sort(key=lambda tup: tup[1])

    for tup in comp_dict['scores']:
      print("\t%s: %s" %tup)

    print("\n")

  def _get_empty_comp(self, comp_type):
    return {"type":comp_type, "scores": []}

comparer = RedditComparer(sys.argv[1:])
posts = comparer.get_comparision_posts()
comments = comparer.get_comparision_comments()
comparer.pretty_print_comparision(posts)
comparer.pretty_print_comparision(comments)