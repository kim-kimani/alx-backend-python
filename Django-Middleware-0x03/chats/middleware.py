# chats/middleware.py
import datetime
import logging
from django.utils.deprecation import MiddlewareMixin

# Set up logging to file
logging.basicConfig(
    filename='requests.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

class RequestLoggingMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        self.get_response = get_response

    def process_request(self, request):
        # This runs before the view is called
        return None  # Continue processing

    def process_response(self, request, response):
        # Get user info
        if request.user.is_authenticated:
            user = request.user.username
        else:
            user = 'Anonymous'

        # Log message
        log_message = f"User: {user} - Path: {request.path}"
        logging.info(log_message)

        return response