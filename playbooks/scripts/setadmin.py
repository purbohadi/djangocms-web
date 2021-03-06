#!/usr/bin/env python
# A script to set the admin credentials
# Assumes two environment variables
#
# PROJECT_DIR: the project directory (e.g., ~/projname)
# ADMIN_PASSWORD: admin user's password

import os
import sys

# Add the project directory to system path
proj_dir = os.path.expanduser(os.environ['PROJECT_DIR'])
sys.path.append(proj_dir)

os.environ['DJANGO_SETTINGS_MODULE'] = 'DjangoCMSDemo.settings'

from django.contrib.auth.models import User
if User.objects.filter(username='admin').exists():
   user = User.objects.get(username='admin')
   user.set_password('b8m3bcId')
   user.is_superuser = True
   user.is_staff = True
   user.save()
else:
   user = User(username='admin')
   user.set_password('b8m3bcId')
   user.is_superuser = True
   user.is_staff = True
   user.save()

   

