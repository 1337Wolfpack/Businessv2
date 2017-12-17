#!/usr/bin/env python


import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "business.settings")
import django
django.setup()



from django.contrib.auth.models import User
User.objects.create_superuser('admin', '', 'sesnv4gk')
