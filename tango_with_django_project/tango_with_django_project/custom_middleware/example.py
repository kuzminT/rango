# coding: utf-8

from django.conf import settings

class ExampleMiddleware:
    def process_request(self, request):
        settings.user_ip = request.META['REMOTE_ADDR']
        # print(settings.user_ip)
        # return None

