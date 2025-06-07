import datetime
from django.http import HttpResponseForbidden
from django.utils.deprecation import MiddlewareMixin

class RestrictAccessByTimeMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Get current server time
        current_time = datetime.datetime.now().time()

        # Define allowed time range: 6:00 PM to 9:00 PM
        start_time = datetime.time(18, 0)  # 6:00 PM
        end_time = datetime.time(21, 0)    # 9:00 PM

        # Check if current time is within allowed window
        if not (start_time <= current_time <= end_time):
            return HttpResponseForbidden("Access to the chat is only allowed between 6:00 PM and 9:00 PM.")

        # Otherwise, proceed with the request
        response = self.get_response(request)
        return response