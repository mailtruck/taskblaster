import query
import urlparse
import urllib


class Url():

  def __init__(self, urlstring):
    tmpurl = urlparse.urlparse(urlstring)
    self.scheme = tmpurl.scheme
    self.hostname = tmpurl.hostname
    self.path = tmpurl.path
    self.params = tmpurl.params
    self.fragment = tmpurl.fragment
    self.query = query.Query(tmpurl.query)


  def tostring(self):
    urlparts = (self.scheme,
               self.hostname,
               self.path,
               self.params,
               self.query.tostring(),
               self.fragment)
    return urlparse.urlunparse(urlparts)

