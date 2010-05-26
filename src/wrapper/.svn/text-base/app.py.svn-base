# Monkeypatches to enable bfg.repoze within GAE
import os; os.mkdir = None # GAE hasn't os.mkdir
import appengine_monkey    # installed by buildout

from google.appengine.ext.webapp.util import run_wsgi_app

# Replace this with your own app
from myapp import run

if __name__ == '__main__':
  settings = {
    'reload_templates': True,
    'debug_authorization': False,
    'debug_notfound': True,
  }
  run_wsgi_app(run.wsgi_app())