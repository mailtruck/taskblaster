import helper


REFERRER_BLACKLIST = ['google']


class ReferrerTagFilter():

  def run(self, request):
    referrer = request.referrer
    if not referrer:
      return
    if not referrer.hostname:
      return

    referrer_tag = helper.get_domain_tag(referrer.hostname)

    for item in REFERRER_BLACKLIST:
      if referrer_tag == item:
        return

    if referrer_tag == request.domain_tag:
      return

    request.referrer_tag = referrer_tag

