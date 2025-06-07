# chats/middleware.py

import datetime
from django.http import HttpResponseForbidden, JsonResponse
from django.utils.deprecation import MiddlewareMixin
from django.utils import timezone


# --- Middleware for Time Restriction ---
class RestrictAccessByTimeMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        now = timezone.localtime(timezone.now())
        current_hour = now.hour

        if not (9 <= current_hour < 18):
            return HttpResponseForbidden(
                "Chat access is only allowed between 9 AM and 6 PM."
            )

        return self.get_response(request)


# --- Middleware for Logging Requests ---
class RequestLoggingMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = request.user.username if request.user.is_authenticated else 'Anonymous'
        log_message = f"User: {user} - Path: {request.path}"

        # Use logging module if you want to write to a file
        import logging
        logger = logging.getLogger(__name__)
        logger.info(log_message)

        return self.get_response(request)


# --- Middleware for Offensive Language Filtering ---
class OffensiveLanguageMiddleware(MiddlewareMixin):
    OFFENSIVE_WORDS = ['badword1', 'badword2', 'damn', 'stupid']  # You can load from file/db too

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Only check POST/PUT/PATCH requests (message creation/update)
        if request.method in ['POST', 'PUT', 'PATCH']:
            try:
                body = request.json() if hasattr(request, 'json') else request.POST
                message_body = body.get('message_body', '') if isinstance(body, dict) else ''
            except Exception:
                message_body = ''

            if any(word in message_body.lower() for word in self.OFFENSIVE_WORDS):
                return JsonResponse(
                    {"error": "Message contains offensive language."},
                    status=400
                )

        return self.get_response(request)