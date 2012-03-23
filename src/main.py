#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import email
import logging
import logsaver
import requestitem
import savelinkhandler
import taskblasteritem
import url
import urllib

from urlparse import urlparse
from google.appengine.api import taskqueue
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.mail_handlers import InboundMailHandler 
from google.appengine.ext.webapp import util


def urlquote(ustr):
  return urllib.quote_plus(unicode(ustr).encode('utf-8'))


def GetRequestItem(request):
  href = request.get('href')
  title = request.get('title')
  referrer = request.get('referrer')
  tags_str = request.get('tags')
  tags = []
  if tags_str:
    tags = tags_str.split(',')

  return requestitem.RequestItem(href, title, referrer, tags) 


def QueueTask(request):
  taskqueue.add(url='/bookmarklet/worker', params={'href': request.href, 'title': request.title, 'referrer': request.referrer, 'tags': ','.join(request.tags)})


class EmailHandler(InboundMailHandler):

  def receive(self, message):
    tags = ['to']

    # TODO: Why is the subject something misformatted?
    title = message.subject

    plaintext = message.bodies(content_type='text/plain')
    for text in plaintext:
      href = text[1].decode()
      break

    request = requestitem.RequestItem(href, title, None, tags)
    QueueTask(request)


class BookmarkletHandler(webapp.RequestHandler):

  def _SaveLink(self, request):
    QueueTask(request)
    self.response.out.write('ok')


  def _NoUser(self, request):
    redirect_url = '/bookmarklet/post?href=%s&title=%s' % (
                   urlquote(request.href), urlquote(request.title))

    referrer = request.referrer
    if referrer:
      redirect_url += '&referrer=' + urlquote(referrer)

    tags = request.tags
    if len(tags):
      redirect_url += '&tags=' + urlquote(','.join(tags))

    self.redirect(users.create_login_url(redirect_url))


  def post(self):
    request = GetRequestItem(self.request)
    user = users.get_current_user()
    if user:
      self._SaveLink(request)
    else:
      self._NoUser(request)


  def get(self):
    user = users.get_current_user()
    if user:
      href = self.request.get('href')
      if href:
        request = GetRequestItem(self.request) 
        self._SaveLink(request)
        self.redirect(href)
      else:
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write('Hello, ' + user.nickname())
    else:
      self.redirect(users.create_login_url(self.request.uri))


class BookmarkletWorker(webapp.RequestHandler):

  def post(self):
    request = GetRequestItem(self.request)
    item = taskblasteritem.TaskblasterItem(request.href, request.title, request.referrer, request.tags)
#    handler = savelinkhandler.SaveLinkHandler(logsaver.LogSaver())
    handler = savelinkhandler.SaveLinkHandler()
    handler.save(item)


def main():
    application = webapp.WSGIApplication([EmailHandler.mapping(),
                                          ('/bookmarklet/post', BookmarkletHandler),
                                          ('/bookmarklet/worker', BookmarkletWorker)],
                                         debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
