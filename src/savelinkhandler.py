import actionfilter
import categoryfilter
import domaintagfilter
import referrertagfilter
import utmfilter
import pinboardsaver
import taglist


class SaveLinkHandler():

  def __init__(self, saver=None):
    self.__filters = [
      utmfilter.UtmFilter(),
      domaintagfilter.DomainTagFilter(),
      referrertagfilter.ReferrerTagFilter(),
      actionfilter.ActionFilter(),
      categoryfilter.CategoryFilter()
    ]
    if not saver:
      saver = pinboardsaver.PinboardSaver()
    self.__saver = saver

  def save(self, request):
    for filter in self.__filters:
      filter.run(request)
    self.__saver.save(request)

