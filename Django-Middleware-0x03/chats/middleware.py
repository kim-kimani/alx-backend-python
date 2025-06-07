# chats/middleware.py

import datetime
from django.http import HttpResponseForbidden
from django.utils.deprecation import MiddlewareMixin

class RestrictAccessByTimeMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Get current time in server's timezone (naive time object)
        now = datetime.datetime.now()
        current_hour = now.hour

        # Allow access only between 9 AM and 6 PM
        if not (9 <= current_hour < 18):
            return HttpResponseForbidden("Chat access is only allowed between 9 AM and 6 PM.")

        return self.get_response(request)