#from django.core.context_processors import request
from django.conf import settings


def user_ip(request):
    return {'user_ip': settings.user_ip}