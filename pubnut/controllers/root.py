from pecan import expose, redirect
from webob.exc import status_map


class RootController(object):

    @expose(generic=True, template='index.html')
    def index(self):
        # return first page of paginated posts
        return dict()

    @expose(generic=True, template='index.html')
    def _default(self, item, *remainder):
        # return a single post or page, search both directories
        print "item is: %s" % item
        return dict(item=item, leftover=remainder)

    @expose('error.html')
    def error(self, status):
        try:
            status = int(status)
        except ValueError:  # pragma: no cover
            status = 500
        message = getattr(status_map.get(status), 'explanation', '')
        return dict(status=status, message=message)
