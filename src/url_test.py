import url
import unittest


class UrlTest(unittest.TestCase):

  def test_empty(self):
    u = url.Url('')
    self.assertEquals('', u.tostring())

  def test_full_url(self):
    u = url.Url('http://www.google.com/foo/bar.html?a=1&b=2#frag')
    self.assertEquals('http', u.scheme)
    self.assertEquals('www.google.com', u.hostname)
    self.assertEquals('/foo/bar.html', u.path)
    self.assertEquals('', u.params)
    self.assertEquals('frag', u.fragment)
    self.assertEquals('a=1&b=2', u.query.tostring())
    self.assertEquals('http://www.google.com/foo/bar.html?a=1&b=2#frag',
                      u.tostring())


if __name__ == '__main__':
    unittest.main()

