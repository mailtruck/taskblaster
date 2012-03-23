class TagList():

  def __init__(self, tags=[]):
    self.__tags = {}
    for tag in tags:
      self.add(tag)

  def add(self, tag):
    if tag is None or len(tag) == 0:
      return False
    if tag not in self.__tags:
      self.__tags[tag] = True
      return True
    return False

  def addAll(self, tags=[]):
    for t in tags:
      self.add(t)
    return True

  def remove(self, tag):
    if tag not in self.__tags:
      return False
    del self.__tags[tag]
    return True

  def size(self):
    return len(self.__tags)

  def list(self):
    buf = []
    for k in self.__tags.iterkeys():
      buf.append(k)
    return buf

  def serialize(self):
    buf = ''
    for k in self.__tags.iterkeys():
      if len(buf) > 0:
        buf += ','
      buf += k
    return buf

