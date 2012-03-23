import query
import unittest

class TestQuery(unittest.TestCase):

  def test_empty(self):
    q = query.Query('')
    self.assertEquals(None, q.get('a'))
    self.assertEquals('', q.tostring())

  def test_single_value(self):
    q = query.Query('a=1')
    self.assertEquals('1', q.get('a'))
    self.assertEquals(1, len(q.keys()))
    q.set('a', '2')
    self.assertEquals('2', q.get('a'))
    self.assertEquals('a=2', q.tostring())
    q.remove('a')
    self.assertEquals('', q.tostring())

  def test_trailing_ampersand(self):
    q = query.Query('a=1&')
    self.assertEquals('1', q.get('a'))
    self.assertEquals(1, len(q.keys()))
    q.set('a', '2')
    self.assertEquals('2', q.get('a'))
    self.assertEquals('a=2', q.tostring())

  def test_empty_value(self):
    q = query.Query('a=1&b')
    self.assertEquals('1', q.get('a'))
    q.set('a', '2')
    self.assertEquals('2', q.get('a'))
    self.assertEquals('a=2&b=', q.tostring())
    self.assertEquals(2, len(q.keys()))
    q.remove('b')
    self.assertEquals('a=2', q.tostring())

  def test_multiple_values(self):
    q = query.Query('a=1&a=2')
    self.assertEquals(['1', '2'], q.get('a'))
    q.add('a', '3')
    self.assertEquals(['1', '2', '3'], q.get('a'))
    self.assertEquals('a=1&a=2&a=3', q.tostring())
    self.assertEquals(1, len(q.keys()))
    q.remove('a')
    self.assertEquals('', q.tostring())


if __name__ == '__main__':
    unittest.main()

