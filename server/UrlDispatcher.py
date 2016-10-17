import re
from server.Exception import NotFoundException


def dispatch_url(request, url_list):
    for url in url_list:
        method, regex, callback = url
        match = regex.search(request.path)
        if request.method == method and match:
            return callback, match.groups()
    raise NotFoundException(request.path)


def url(method, regex, callback):
    return method, re.compile(regex), callback
