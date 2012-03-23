CATEGORIES = {
  u'priority': [u'avc', u'codinghorror', u'dashes', u'marco', u'nczonline', u'rc3'],
  u'news': [u'atlantic', u'economist', u'newyorker', u'npr', u'nymag', u'nytimes', u'online.wsj', u'techcrunch', u'techdirt', u'theatlantic', u'theverge', u'thedailybeast', u'vanityfair', u'wired', u'wsj'],
  u'tech': [u'apigee', u'arstechnica', u'html5rocks']
}


class CategoryFilter():

  def _getcategory(self, domain_tag):
    for tag, domains in CATEGORIES.iteritems():
      for domain in domains:
        if domain_tag.find(domain) > -1:
          return tag
    return None

  
  def run(self, request):
    category = self._getcategory(request.domain_tag)
    if category:
      request.tags.add(u'c:' + category)

