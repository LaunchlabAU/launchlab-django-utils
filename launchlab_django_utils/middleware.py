from django.http import HttpResponsePermanentRedirect

try:
    from django.utils.deprecation import MiddlewareMixin
except ImportError:
    class MiddlewareMixin(object):
        """
        If this middleware doesn't exist, this is an older version of django
        and we don't need it.
        """
        pass


class RemoveWWW(MiddlewareMixin):
    def process_request(self, request):
        try:
            if request.META['HTTP_HOST'].lower().find('www.') == 0:
                return HttpResponsePermanentRedirect(request.build_absolute_uri().replace('://www.', '://'))
        except:
            pass
        return None
