from http.server import BaseHTTPRequestHandler
import json
import re


def url(method, route, callback):
    return method, re.compile(route), callback


def handle_test(request):
    return {'Message': request}


urls = [
    url('GET', r'^/test', handle_test)
]


class RequestHandler(BaseHTTPRequestHandler):
    def create_request_object(self):
        return {
            "verb": self.command,
            "path": self.path
        }

    def unknown_route_error(self):
        return {"error": "Unknown route {}".format(self.path)}

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/json')
        self.end_headers()

        response = self.unknown_route_error()
        for url in urls:
            verb, regex, callback = url
            if regex.match(self.path) and self.command == verb:
                response = callback(self.create_request_object())
                break

        message = json.dumps(response)

        self.wfile.write(bytes(message, "utf8"))
