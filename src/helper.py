PREFIX = ['blog', 'blogs', 'www']

SUFFIX = ['appspot.com', 'blogspot.com', 'tumblr.com', 'wordpress.com', 'com', 'edu', 'net', 'org']


def get_domain_tag(domain):
  for item in PREFIX:
    if domain.startswith(item + '.'):
      pos = len(item) + 1
      domain = domain[pos:]
      break
    
  for item in SUFFIX:
    if domain.endswith('.' + item):
      pos = len(domain) - len(item) - 1
      domain = domain[:pos]

  return domain

