class HTTPException(Exception):
    code = None


class NotFoundException(HTTPException):
    code = 404

    def __init__(self, route_name=''):
        super(NotFoundException, self).__init__('Route was not found: {}'.format(route_name))
        self.route_name = route_name
