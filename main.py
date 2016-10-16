from server import SocketInterface, HTTPServer
from server.UrlDispatcher import url, dispatch_url
from server.HTTPServer import HTTPResponse
import json

print("Starting server")
socket_interface = SocketInterface()
print('Server has started on {ip}:{socket}!'.format(ip=socket_interface.ip, socket=socket_interface.port_number))


def get_test(request, number):
    return {'number': number}

url_list = [
    url('GET', r'/test/([0-9]+)', get_test)
]


def handle_request(request):
    decoded = request.decode('utf8')
    request_object = HTTPServer.parse_http_request(decoded)

    dispatch_result = dispatch_url(request_object, url_list)

    if not dispatch_result:
        return 'path not found'

    callback, params = dispatch_result

    response = HTTPResponse(
        payload=json.dumps(callback(request_object, *params))
    )

    return response.create_response_string()


while True:
    socket_interface.handle_request(handle_request)
