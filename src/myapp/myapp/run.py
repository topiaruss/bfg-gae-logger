from repoze.bfg.configuration import Configurator
from myapp.models import get_root

def wsgi_app(**settings):
  config = Configurator(root_factory=get_root, settings=settings)
  config.load_zcml('configure.zcml')
  return config.make_wsgi_app()