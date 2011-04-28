# Created by Neil McCarthy, Implementation Engineer, Yammer, nmccarthy@yammer-inc.com
# v0.1, 04/20/2011

import sys, httplib, simplejson

# here is the oath token, replace it with your own
oauthToken= 'pasteyouroauthtokeninsidethesequotes'

# initiate connection to Yammer (must be https)
yamconn = httplib.HTTPSConnection("www.yammer.com")

# find user by email address so we can get their id
findEndPoint='/api/v1/users/by_email.json?access_token=' + oauthToken + '&email=' + sys.argv[1]
yamconn.request('GET', findEndPoint)

# process json from yammer.com -> convert to python dict
userraw=yamconn.getresponse()
userread=userraw.read()
user=simplejson.loads(userread)

# get the id of the user and build the deletion endpoint
userIdToDelete = user[0]['id']
deleteEndPoint = '/api/v1/users/' + str(userIdToDelete) + '.json?access_token=' + oauthToken

# send delete command to yammer api
yamconn.request('DELETE', deleteEndPoint)

# show status
deleteraw=yamconn.getresponse()
print str(deleteraw.status) + ' ' + str(deleteraw.reason)

# close https connection
yamconn.close()