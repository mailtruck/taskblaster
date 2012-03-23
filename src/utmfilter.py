class UtmFilter():

  def run(self, request):
    url = request.url
    query = url.query
    for k in query.keys():
      if k.startswith('utm_'):
        query.remove(k)

