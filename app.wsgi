import sys
import site
import os

site.addsitedir('/var/www/kantine/env/lib/python3.13/site-packages')

sys.path.insert(0, '/var/www/kantine')

os.chdir('/var/www/kantine')

os.environ['VIRTUAL_ENV'] = '/var/www/kantine/env'
os.environ['PATH'] = '/var/www/kantine/env/bin:' + os.environ['PATH']

from app import app as application
