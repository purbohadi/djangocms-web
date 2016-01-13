#!/usr/bin/env python

import sys
import os
import os.path
import logging
import time
import shutil
import glob
from datetime import datetime

# Add the project directory to system path
proj_dir = os.path.expanduser(os.environ['PROJECT_DIR'])
sys.path.append(proj_dir)

os.environ['DJANGO_SETTINGS_MODULE'] = 'DjangoCMSDemo.settings'

from django.conf import settings
from django.db import connection

DATABASE_NAME = connection.settings_dict['NAME']
DATABASE_USER = connection.settings_dict['USER']
DATABASE_PASSWORD = connection.settings_dict['PASSWORD']

logging.basicConfig(level=logging.INFO, stream=sys.stdout)

BACKUP_DIR = "backup" #os.path.join(proj_dir, "/backup/")  #"%s/backups" % os.path.dirname(__file__)
CONFIG_DIR = BACKUP_DIR+"/config"
DB_DIR = BACKUP_DIR+"/db"
MYSQL_CMD = 'mysqldump'
CONFIG_FILE = proj_dir+"/DjangoCMSDemo/settings.py"

def _setup():
    if not os.path.exists(BACKUP_DIR):
        logging.debug("Created backup directory %s" % BACKUP_DIR)
        os.mkdir(BACKUP_DIR)
	os.mkdir(DB_DIR)
	os.mkdir(CONFIG_DIR)
    else:
        logging.debug("Using backup directory %s" % BACKUP_DIR)
    
def _backup_name():
    now = datetime.now()
    day_name = now.strftime("%A")
    file_name = "%s.sql" % time.strftime('%m%d%Y-%H%M%S').lower() 
    logging.debug("Setting backup name for day name %s as %s" % (time.strftime('%m%d%Y-%H%M%S'), file_name))
    return file_name

def _run_backup(file_name):
    cmd = "%(mysqldump)s -u %(user)s --password=%(password)s %(database)s > %(log_dir)s/%(file)s" % {
        'mysqldump' : MYSQL_CMD,
        'user' : DATABASE_USER,
        'password' : DATABASE_PASSWORD,
        'database' : DATABASE_NAME,
        'log_dir' : DB_DIR,
        'file': file_name}

    config_filename = "%s" % time.strftime('%m%d%Y-%H%M%S').lower() +".py"
    CONFIG_PATH = os.path.expanduser(os.path.join('~'+'/'+CONFIG_DIR, config_filename))
    shutil.copyfile(CONFIG_FILE, CONFIG_PATH)
    logging.debug("Backing up with command %s " % cmd)
    return os.system(cmd)

def _check_and_validate_files(file_name):
    DB_PATH = os.path.expanduser("~/"+DB_DIR)
    db_files = sorted(os.listdir(DB_PATH), key=lambda x: os.path.getctime(os.path.join(DB_PATH,x)))
    if(len(db_files) < 7):
	_run_backup(file_name)
    else:
	CONFIG_PATH = os.path.expanduser("~/"+CONFIG_DIR)
    	config_files = sorted(os.listdir(CONFIG_PATH), key=lambda x: os.path.getctime(os.path.join(CONFIG_PATH,x)))			    
	os.remove(os.path.join(CONFIG_PATH, config_files[0]))
	os.remove(os.path.join(DB_PATH, db_files[0]))
	_run_backup(file_name)	


def main(*args):
    _setup()
    file_name = _backup_name()
    _check_and_validate_files(file_name)
#    _run_backup(file_name)
        
    
if __name__ == '__main__':
    sys.exit(main(*sys.argv))    
