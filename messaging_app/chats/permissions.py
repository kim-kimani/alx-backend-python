# chats/permissions.py
from rest_framework import permissions
from .models import Conversation, Message

class IsParticipantOfConversation(permissions.BasePermission):
    """
    Custom permission to only allow participants of a conversation to access messages.
    Assumes the view has a get_object() method that returns a Message or Conversation.
    """

    def has_permission(self, request, view):
        # Only authenticated users can access the API
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # If the object is a Message, check its conversation's participants
        if isinstance(obj, Message):
            return request.user in obj.conversation.participants.all()
        
        # If the object is a Conversation
        elif isinstance(obj, Conversation):
            return request.user in obj.participants.all()

        return False