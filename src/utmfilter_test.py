import taskblasteritem
import utmfilter
import url
import unittest

class TestUtmFilter(unittest.TestCase):

  def test_remove_query(self):
    href= 'http://www.monsur.com/foo?utm_abc=1&utm_def=2&foo=bar'
    request = taskblasteritem.TaskblasterItem(href)

    filter = utmfilter.UtmFilter()
    filter.run(request)

    self.assertEquals('http://www.monsur.com/foo?foo=bar',
                      request.url.tostring())


if __name__ == '__main__':
    unittest.main()

