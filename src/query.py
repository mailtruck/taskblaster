import urllib
try:
   from urlparse import parse_qs
except ImportError:
   from cgi import parse_qs


class Query():

  def __init__(self, querystring):
    self.__querydict = parse_qs(querystring, True)

  
  def get(self, key):
    val = self.__querydict.get(key)
    if val is None:
      return val
    if len(val) == 1:
      return val[0]
    return val


  def set(self, key, val):
    if not isinstance(val, list):
      val = [val]
    self.__querydict[key] = val


  def add(self, key, val):
    existing = self.__querydict[key]
    if not existing:
      existing = []
    existing.append(val)
    self.set(key, existing)

  
  def remove(self, key):
    del self.__querydict[key]


  def keys(self):
    return self.__querydict.keys()


  def _pairtostring(self, key, val, querystr):
    if len(querystr) > 0:
      querystr.append('&')
    querystr.append(urllib.quote_plus(key))
    if val is None:
      return
    querystr.append('=')
    querystr.append(urllib.quote_plus(val))
    

  def tostring(self):
    querystr = []
    for k,v in self.__querydict.items():
      if v is None:
        self._pairtostring(k, v, querystr)
      elif len(v) == 1:
        self._pairtostring(k, v[0], querystr)
      else:
        for subv in v:
          self._pairtostring(k, subv, querystr)
    return ''.join(querystr)

