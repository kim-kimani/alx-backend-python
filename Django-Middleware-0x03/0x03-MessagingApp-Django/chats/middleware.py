import logging
import datetime
from django.utils.deprecation import MiddlewareMixin

# Configure logger
logger = logging.getLogger(__name__)

class RequestLoggingMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        # Get user information
        user = request.user if request.user.is_authenticated else 'Anonymous'
        
        # Log the request
        logger.info(f"{datetime.datetime.now()} - User: {user} - Path: {request.path}")
        
        # Process the request
        response = self.get_response(request)
        
        return response