import taglist
import url


class TaskblasterItem():

  def __init__(self, href, title=None, referrer=None, tags=[]):
    self.url = url.Url(href)

    t = title
    if t is None:
      t = href
    self.title = t

    self.tags = taglist.TagList(tags)

    r = None
    if referrer:
      r = url.Url(referrer)
    self.referrer = r

    self.action = None
    self.domain_tag = None
    self.referrer_tag = None

