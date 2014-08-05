import os.path

from pyramid.paster import get_app
from pyramid.paster import setup_logging

here = os.path.dirname(os.path.abspath(__file__))
inipath = os.path.join(here, 'development.ini')

setup_logging(inipath)
application = get_app(inipath)
