import taglist
import pinboard

class PinboardSaver():

  def __init__(self):
    self.__p = pinboard.open('$PINBOARDUSERNAME', '$PINBOARDPASSWORD')

  def _gettags(self, request):
    tags = taglist.TagList()
    tags.add(request.action)
    tags.add(request.domain_tag)
    tags.add(request.referrer_tag)
    tags.addAll(request.tags.list())
    return tags.list() 

  def save(self, request):
    href = request.url.tostring()
    title = request.title
    tags = self._gettags(request)
    self.__p.add(href, title, tags=tags)

