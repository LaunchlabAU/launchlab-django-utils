from django.conf import settings


def debug(request):
    """
    Override django.template.context_processors.debug

    Intended use case: Ignore INTERNAL_IPS when using vagrant.
    """
    return {'debug': settings.DEBUG}
