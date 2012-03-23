DEFAULT_ACTION = u'read'

ADDITIONAL_ACTIONS = {
  u'watch': [u'youtube', u'vimeo'],
  u'hack': [u'github']
}


class ActionFilter():

  def _getaction(self, domain_tag):
    for tag, domains in ADDITIONAL_ACTIONS.iteritems():
      for domain in domains:
        if domain_tag.find(domain) > -1:
          return tag
    return DEFAULT_ACTION

  
  def run(self, request):
    request.action = self._getaction(request.domain_tag)

