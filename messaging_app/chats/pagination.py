# chats/pagination.py
from rest_framework.pagination import PageNumberPagination


class StandardResultsSetPagination(PageNumberPagination):
    """
    A standard pagination class for chat messages/conversations.
    
    Uses page-based pagination. Internally uses `page.paginator.count`
    to determine total number of items.
    """
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100