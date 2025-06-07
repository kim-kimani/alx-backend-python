import time
from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin

class RateLimitMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        self.get_response = get_response
        # Dictionary to store request timestamps by IP
        self.request_logs = {}  # { "ip": [timestamp1, timestamp2, ...] }

    def __call__(self, request):
        ip = self._get_client_ip(request)

        # Only rate-limit POST requests to chat endpoints
        if request.path.startswith('/api/messages/') and request.method == 'POST':
            now = time.time()
            window_start = now - 60  # 1 minute window

            # Initialize log for this IP if not present
            if ip not in self.request_logs:
                self.request_logs[ip] = []

            # Keep only requests within the last 60 seconds
            self.request_logs[ip] = [t for t in self.request_logs[ip] if t >= window_start]

            if len(self.request_logs[ip]) >= 5:
                return JsonResponse({
                    'error': 'Too many requests. You can send up to 5 messages per minute.'
                }, status=429)

            # Record this request
            self.request_logs[ip].append(now)

        response = self.get_response(request)
        return response

    def _get_client_ip(self, request):
        """Helper to extract client IP from request"""
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0].strip()
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip