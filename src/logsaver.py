import logging


class LogSaver():

  def save(self, request):
    logging.info('Saving %s (%s)' % (request.url.tostring(), request.title))

