# -*- coding: utf-8 -*-
#Use this tool to add admin users. Usage: python add_admin.py <username> <password>
#If the user already exists, its password will be changed
#This code can only be run on the server.
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "setenta.settings")
import sys
from setenta_members.models import Admins
from django.contrib.auth import hashers
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()

username = sys.argv[1]
password = sys.argv[2]

try:
	#User exists -> update password
	user = Admins.objects.get(username=username)
	user.password = hashers.make_password(password)
	user.save()
	print "Password updated for " + username +"."
except:
	#User doesn't exist
	user = Admins(username=username,password=hashers.make_password(password))
	user.save()
	print "A new user " + username + " was added."

