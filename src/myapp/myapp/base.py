# http://bfg.repoze.org/pastebin/684
class SimpleResponse:
    """ Faster than webob.Response """
    status = "200 OK"
    def __init__(self, body, content_type="text/html"):
        self.app_iter = [body]
        self.headerlist = [("Content-Type", content_type),
                           ("Content-Length", str(len(body)))]
import os
here = os.path.dirname(__file__)
icon = open(os.path.join(here, "images/favicon.ico")).read()
icon_response = SimpleResponse(icon, "image/x-icon")

def favicon(context, request):
    return icon_response

def robots(context, request):
    return SimpleResponse("")