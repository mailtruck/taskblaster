from taglist import TagList
import unittest


class TagListTest(unittest.TestCase):

  def test_new(self):
    taglist = TagList()
    self.assertEquals(0, taglist.size())
    self.assertEquals('', taglist.serialize())

    val = taglist.add(None)
    self.assertFalse(val)
    self.assertEquals(0, taglist.size())
    val = taglist.add('')
    self.assertFalse(val)
    self.assertEquals(0, taglist.size())
    self.assertEquals(0, len(taglist.list()))

    val = taglist.add('foo')
    self.assertTrue(val)
    self.assertEquals(1, taglist.size())
    self.assertEquals('foo', taglist.serialize())
    val = taglist.add('foo')
    self.assertFalse(val)
    self.assertEquals(1, taglist.size())

    val = taglist.add('bar')
    self.assertTrue(val)
    self.assertEquals(2, taglist.size())
    self.assertEquals('foo,bar', taglist.serialize())
    self.assertEquals(2, len(taglist.list()))

    val = taglist.remove('baz')
    self.assertFalse(val)
    val = taglist.remove('bar')
    self.assertTrue(val)
    val = taglist.remove('foo')
    self.assertTrue(val)
    val = taglist.remove('foo')
    self.assertFalse(val)

    taglist.addAll(['one', 'two', 'three'])
    self.assertEquals(3, taglist.size())

  def test_initialvalues(self):
    taglist = TagList(['foo', 'bar'])
    self.assertEquals(2, taglist.size())


if __name__ == '__main__':
  unittest.main()

