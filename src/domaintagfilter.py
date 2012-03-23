import helper

class DomainTagFilter():

  def run(self, request):
    domain_tag = helper.get_domain_tag(request.url.hostname)
    if domain_tag:
      request.domain_tag = domain_tag

