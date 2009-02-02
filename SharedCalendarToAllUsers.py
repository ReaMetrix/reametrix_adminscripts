try:
  from xml.etree import ElementTree # for Python 2.5 users
except ImportError:
  from elementtree import ElementTree
import gdata.service
import atom.service
import atom
import getopt
import sys
import string
import time
import urllib
import gdata.auth
import gdata.calendar
import gdata.calendar.service
import gdata.apps
import gdata.apps.service

account = gdata.apps.service.AppsService('admin user','secret','reametrix.com')
account.ProgrammaticLogin()

users=account.RetrieveAllUsers()
calendar_service = gdata.calendar.service.CalendarService()
calendar_service.email = 'admin user'
calendar_service.password = 'secret'
calendar_service.ProgrammaticLogin()

for user in users.entry:
#  print s.login.user_name
  rule = gdata.calendar.CalendarAclEntry()
  rule.scope = gdata.calendar.Scope(value=user.login.user_name+'@reametrix.com', scope_type='user')
  roleValue = 'http://schemas.google.com/gCal/2005#%s' % ('read')
  rule.role = gdata.calendar.Role(value=roleValue)
  aclUrl = '/calendar/feeds/calendar id/acl/full'
  try:
    returned_rule =calendar_service.InsertAclEntry(rule, aclUrl)
  except gdata.service.RequestError:
    print "Share already exists"

  print user.login.user_name



#user = 'sheri@reametrix.com'
#params = urllib.urlencode({'max-results': 50, 'xoauth_requestor_id': user})
#uri = '%s?%s' % (CALENDAR_URL, params)
