from server import SocketInterface
from server.UrlDispatcher import url
from server.HTTPServer import JSONRequestHandler


def get_test(request, number):
    return {'number': number}

url_list = [
    url('GET', r'/test/([0-9]+)', get_test)
]

print("Starting server")
socket_interface = SocketInterface()
print('Server has started on {ip}:{socket}!'.format(ip=socket_interface.ip, socket=socket_interface.port_number))
socket_interface.server_forever(JSONRequestHandler(urls=url_list).handle_request)
