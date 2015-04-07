# -*- coding: utf-8 -*-
#This is a cron job that should be running on a daily basis
#It clears expired authorizations and sessions
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "setenta.settings")
import sys
from setenta_members.models import Authorizations
from django.core.wsgi import get_wsgi_application
from django.utils import timezone
from django.contrib.sessions.models import Session

application = get_wsgi_application()

expired_auths = Authorizations.objects.filter(expirity__lte=timezone.now())
expired_auths.delete()

expired_sessions = Session.objects.filter(expire_date=timezone.now())
expired_sessions.delete()

