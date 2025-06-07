# chats/filters.py
import django_filters
from .models import Message, Conversation
from django.contrib.auth import get_user_model

User = get_user_model()

class MessageFilter(django_filters.FilterSet):
    conversation_with = django_filters.ModelChoiceFilter(
        queryset=User.objects.all(),
        method='filter_by_conversation_with',
        label='Conversation with User'
    )
    sent_after = django_filters.DateTimeFilter(field_name='sent_at', lookup_expr='gte')
    sent_before = django_filters.DateTimeFilter(field_name='sent_at', lookup_expr='lte')

    class Meta:
        model = Message
        fields = ['conversation', 'sender', 'sent_after', 'sent_before', 'conversation_with']

    def filter_by_conversation_with(self, queryset, name, value):
        # Get all conversations where both the current user and the target user are participants
        return queryset.filter(
            conversation__participants=self.request.user
        ).filter(
            conversation__participants=value
        ).distinct()