class RedditEntry(object):
  """
  Base class for both comments and posts.
  """

  def __init__(self, data):
    """
    Initializes data dictionary.
    """
    if data is None:
      raise AttributeError("No data given")

    self.data = data

  def get_score(self):
    return self._get_data("score")

  def _get_data(self, item):
    return self.data[item]    

  def __str__(self):
    return self.data.__str__()

#Some (so far) unnecessary subclasses
class RedditPost(RedditEntry):
  def __init__(self, data):
    super(self.__class__, self).__init__(data)

class RedditComment(RedditEntry):
  def __init__(self, data):
    super(self.__class__, self).__init__(data)